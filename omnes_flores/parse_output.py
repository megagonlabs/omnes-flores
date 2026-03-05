import re

def parse_output_lines(output_configs, output_lines) -> list[dict]:
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
                    result[key] = _parse_fields(config.get("format"), config["fields"], lines)
                else:
                    result[key] = lines
    return result


def _parse_fields(format_config, field_configs, lines):
    format = _format_func(format_config)
    records = []
    for line in lines:
        fields = {}
        records.append(fields)
        r = format(line)
        for field_config in field_configs:
            if field_config.get("auto_correct") == "begin_from_1":
                v = len(records)
            else:
                v = r[field_config["index"]]
            if field_config.get("type") == "int":
                v = int(v)
            fields[field_config["name"]] = v
    return records


def _format_func(format_config):
    return {
        None: lambda line: line,
        "tsv": lambda line: line.split("\t"),
        "re.findall": lambda line: re.findall(format_config["pattern"], line),
    }[format_config["type"]]


def _test():
    import tomllib
    with open("omnes_flores/resources/40-lang-41-treebank.toml", "rb") as fin:
        config = tomllib.load(fin)

    output_configs = config["ls"]["dialog_template"]["outputs"]
    output_lines = """Japanese

これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。
幸福の科学側からは,特にどうしてほしいという要望はいただいていません。
星取り参加は当然とされ,不参加は白眼視される。
室長の対応には終始誠実さが感じられた。
多くの女性が生理のことで悩んでいます。
先生の理想は限りなく高い。
それは兎も角,私も明日の社説を楽しみにしております。
そうだったらいいなあとは思いますが,日本学術会議の会長談話について“当会では,標記の件について,以下のように考えます。”
教団にとっては存続が厳しくなると思う。
しかし強制していなくても問題です
民族派のみなさんにとって陛下はいちばん大切な方ですから,その霊言について“あり得ない”という前提でお話をされる。
新しい産業構造を作らなければいけない。
心がないんだ。
""".rstrip("\n").split("\n")
    print(parse_output_lines(output_configs, output_lines))

    output_configs = config["wx"]["dialog_template"]["outputs"]
    output_lines = """1	これ	代名詞
2	に	助詞-格助詞
3	不快感	名詞-普通名詞-一般
4	を	助詞-格助詞
5	示す	動詞-一般-五段-サ行
6	住民	名詞-普通名詞-一般
7	は	助詞-係助詞
8	い	動詞-一般-上一段-ア行
9	まし	助動詞-助動詞-マス
10	た	助動詞-助動詞-タ
11	が	助詞-接続助詞
12	,	補助記号-読点
13	現在	副詞
14	,	補助記号-読点
15	表立っ	動詞-一般-五段-タ行
16	て	助詞-接続助詞
17	反対	名詞-普通名詞-一般
18	や	助詞-副助詞
19	抗議	名詞-普通名詞-一般
20	の	助詞-格助詞
21	声	名詞-普通名詞-一般
22	を	助詞-格助詞
23	挙げ	動詞-一般-下一段-ガ行
24	ている	助動詞-上一段-ア行
25	住民	名詞-普通名詞-一般
26	は	助詞-係助詞
27	い	動詞-一般-上一段-ア行
28	ない	助動詞-助動詞-ナイ
29	よう	形状詞-助動詞語幹
30	です	助動詞-助動詞-デス
31	。	補助記号-句点
""".rstrip("\n").split("\n")
    print(parse_output_lines(output_configs, output_lines))

    output_configs = config["ud"]["dialog_template"]["outputs"]
    output_lines = """1	PRON	5	obl
2	ADP	1	case
3	NOUN	5	obj
4	ADP	3	case
5	VERB	6	acl
6	NOUN	8	nsubj
7	ADP	6	case
8	VERB	27	advcl
9	AUX	8	aux
10	AUX	8	aux
11	SCONJ	8	mark
12	PUNCT	8	punct
13	ADV	27	advmod
14	PUNCT	13	punct
15	VERB	23	advcl
16	SCONJ	15	mark
17	NOUN	19	nmod
18	ADP	17	case
19	NOUN	21	nmod
20	ADP	19	case
21	NOUN	23	obj
22	ADP	21	case
23	VERB	25	acl
24	AUX	23	aux
25	NOUN	27	nsubj
26	ADP	25	case
27	VERB	0	root
28	AUX	27	aux
29	AUX	27	aux
30	AUX	27	aux
31	PUNCT	27	punct
""".rstrip("\n").split("\n")
    print(parse_output_lines(output_configs, output_lines))


if __name__ == "__main__":
    _test()
