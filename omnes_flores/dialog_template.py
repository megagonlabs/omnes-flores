import re

from .utils import print_log


def apply_template(dialog_template, records):
    dialogs = []
    for r in records:
        text = r.get("TEXT")
        language = r.get("LANGUAGE")
        sentence = r.get("SENTENCE")
        tokens = r.get("TOKENS")
        messages = []
        for message in dialog_template["messages"]:
            role = message["role"]
            template = message["template"]
            prev = 0
            content = ""
            for match in re.finditer(r"<<<([^>:]+)>>>|<<<([^>:]+):([^>]*)>>>", template):
                for meta_name, target in [
                    ["TEXT", text],
                    ["LANGUAGE", language],
                    ["SENTENCE", sentence],
                    ["TOKEN_NUM", len(tokens)] if tokens else 0,
                    ["TOKEN_TSV", tokens],
                ]:
                    if meta_name == match.group(1):
                        content += template[prev:match.start()]
                        content += str(target)
                        prev = match.end()
                        break
                    if meta_name == match.group(2):
                        fields = match.group(3).split("_")
                        content += template[prev:match.start()]
                        content += "\n".join("\t".join(str(t[f]) for f in fields if f in t) for _, t in enumerate(tokens))
                        prev = match.end()
                        break
                else:
                    assert False, f"meta field not replaced: {match.group(0)}, {template}"
            messages.append({"role": role, "content": content + template[prev:]})
        dialogs.append(messages)
    return dialogs


def parse_output_lines(output_configs, output_text) -> list[dict]:
    output_lines = output_text.rstrip("\n").split("\n")
    result = {}
    for output_config in output_configs:
        for key, config in output_config.items():
            if "line_index" in config:
                assert "line_begin" not in config, "Both line_index and line_begin specified: {config}"
                line = output_lines[config["line_index"]]
                if "fields" in config:
                    result[key] = _parse_fields(config.get("format"), config["fields"], [line])[0]
                else:
                    result[key] = line
            elif "line_begin" in config:
                lines = output_lines[config["line_begin"]:]
                if "fields" in config:
                    result[key] = parse_fields(config.get("format"), config["fields"], lines)
                else:
                    result[key] = lines
    return result


def parse_fields(format_config, field_configs, lines):
    record_parser = format_func(format_config)
    records = []
    for line in lines:
        fields = {}
        r = record_parser(line)
        for field_config in field_configs:
            try:
                if field_config.get("auto_correct") == "begin_from_1":
                    v = len(records)
                else:
                    v = r[field_config["index"]]
                if field_config.get("type") == "int":
                    v = int(v)
                fields[field_config["name"]] = v
            except Exception as e:
                if "fallback" in field_config:
                    print_log(f"fallbacking {field_config['name']} to {field_config['fallback']}: {line}")
                    fields[field_config["name"]] = field_config["fallback"]
                else:
                    print_log(f"unrecoverable error in {field_config['name']}: {line}")
                    raise e
        else:
            records.append(fields)
    return records


def format_func(format_config):
    return {
        None: lambda line: line,
        "tsv": lambda line: line.split("\t"),
        "re.findall": lambda line: re.findall(format_config["pattern"], line),
    }[format_config["type"]]
