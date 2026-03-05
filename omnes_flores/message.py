import re


def apply_template(dialog_template, records):
    dialogs = []
    for r in records:
        text = r.get("text")
        language = r.get("language")
        sentence = r.get("sentence")
        tokens = r.get("tokens")
        messages = []
        for message in dialog_template["messages"]:
            role = message["role"]
            template = message["template"]
            prev = 0
            context = ""
            for match in re.finditer(r"<<<([^>:]+)>>>|<<<([^>:]+):([^>]*)>>>", template):
                for meta_name, target in [
                    ["TEXT", text],
                    ["LANGUAGE", language],
                    ["SENTENCE", sentence],
                    ["TOKEN_NUM", len(tokens)] if tokens else 0,
                    ["TOKEN_TSV", tokens],
                ]:
                    if meta_name == match.group(1):
                        context += template[prev:match.start()]
                        context += str(target)
                        prev = match.end()
                        break
                    if meta_name == match.group(2):
                        fields = match.group(3).split("_")
                        context += template[prev:match.start()]
                        context += "\n".join("\t".join(str(t[f]) for f in fields if f in t) for _, t in enumerate(tokens))
                        prev = match.end()
                        break
                else:
                    assert False, f"meta field not replaced: {match.group(0)}, {template}"
            messages.append({"role": role, "context": context + template[prev:]})
        dialogs.append(messages)
    return dialogs


def _test():
    import tomllib
    with open("omnes_flores/resources/40-lang-41-treebank.toml", "rb") as fin:
        config = tomllib.load(fin)

    template = config["ls"]["dialog_template"]
    print(apply_template(template, [{"text": "This is a test text document."}]))

    template = config["wx"]["dialog_template"]
    print(apply_template(template, [{
        "language": "English",
        "sentence": "This is a test sentence.",
    }]))

    template = config["ud"]["dialog_template"]
    print(apply_template(template, [{
        "language": "English",
        "sentence": "This is a test sentence.",
        "tokens": [
            {"INDEX": 1, "FORMWS": "This "},
            {"INDEX": 2, "FORMWS": "is "},
            {"INDEX": 3, "FORMWS": "a "},
            {"INDEX": 4, "FORMWS": "test "},
            {"INDEX": 5, "FORMWS": "sentence"},
            {"INDEX": 6, "FORMWS": "."},
        ]
    }]))

if __name__ == "__main__":
    _test()
