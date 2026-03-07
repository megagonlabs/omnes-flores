import sys
import tomllib

from transformers import AutoTokenizer

from .dialog_template import apply_template, parse_output_lines
from .inference_vllm import InferenceVLLM
from .cli import add_args


main_adapter_name_or_path = "megagonlabs/omnes-flores-40-lang-41-treebank-v0"


def _test_apply_template():
    tokenizer = AutoTokenizer.from_pretrained(main_adapter_name_or_path)
    config = tokenizer.init_kwargs["_custom"]["omnes-flores"]

    template = config["pipeline"]["LS"]["dialog_template"]
    print(apply_template(template, [{"TEXT": "This is a test text document."}]))

    template = config["pipeline"]["WX"]["dialog_template"]
    print(apply_template(template, [{
        "LANGUAGE": "English",
        "SENTENCE": "This is a test sentence.",
    }]))

    template = config["pipeline"]["UD"]["dialog_template"]
    print(apply_template(template, [{
        "LANGUAGE": "English",
        "SENTENCE": "This is a test sentence.",
        "TOKENS": [
            {"ID": 1, "FORMWS": "This "},
            {"ID": 2, "FORMWS": "is "},
            {"ID": 3, "FORMWS": "a "},
            {"ID": 4, "FORMWS": "test "},
            {"ID": 5, "FORMWS": "sentence"},
            {"ID": 6, "FORMWS": "."},
        ]
    }]))


def _test_parse_output_lines():
    tokenizer = AutoTokenizer.from_pretrained(main_adapter_name_or_path)
    config = tokenizer.init_kwargs["_custom"]["omnes-flores"]

    template = config["pipeline"]["LS"]["dialog_template"]
    print(apply_template(template, [{"TEXT": "This is a test text document."}]))

    template = config["pipeline"]["WX"]["dialog_template"]
    print(apply_template(template, [{
        "LANGUAGE": "English",
        "SENTENCE": "This is a test sentence.",
    }]))

    template = config["pipeline"]["UD"]["dialog_template"]
    print(apply_template(template, [{
        "LANGUAGE": "English",
        "SENTENCE": "This is a test sentence.",
        "TOKENS": [
            {"ID": 1, "FORMWS": "This "},
            {"ID": 2, "FORMWS": "is "},
            {"ID": 3, "FORMWS": "a "},
            {"ID": 4, "FORMWS": "test "},
            {"ID": 5, "FORMWS": "sentence"},
            {"ID": 6, "FORMWS": "."},
        ]
    }]))


def _test_InferenceVLLM():
    args = add_args().parse_args()
    model = InferenceVLLM(args.main_adapter, args)

    template = model.config["pipeline"]["LS"]["dialog_template"]
    ls_batch = [{"TEXT": "This is a test text document."}]
    print("batch:", *ls_batch, sep="\n")
    ls_contexts = apply_template(template, ls_batch)
    print("context:", *ls_contexts, sep="\n")
    print(*model.dump_prompt_tokens(ls_contexts), sep="\n")
    batch_outputs = model.completion(ls_contexts, model.config["pipeline"]["LS"]["adapter"])
    content_texts = [_.outputs[0].text for _ in batch_outputs]
    print("outputs:", *content_texts, sep="\n")
    ls_results = [parse_output_lines(template["outputs"], _) for _ in content_texts]
    for result in ls_results:
        print("LANGUAGE:", result["LANGUAGE"], "SENTENCES:", *result["SENTENCES"], sep="\n")

    template = model.config["pipeline"]["WX"]["dialog_template"]
    wx_batch = [
        {
            "LANGUAGE": r["LANGUAGE"],
            "SENTENCE": sentence,
        } for r in ls_results for sentence in r["SENTENCES"]
    ]
    print("batch:", *wx_batch, sep="\n")
    wx_contexts = apply_template(template, wx_batch)
    print("context:", *wx_contexts, sep="\n")
    print(*model.dump_prompt_tokens(wx_contexts), sep="\n")
    batch_outputs = model.completion(wx_contexts, model.config["pipeline"]["WX"]["adapter"])
    content_texts = [_.outputs[0].text for _ in batch_outputs]
    print("outputs:", *content_texts, sep="\n")
    wx_results = [parse_output_lines(template["outputs"], _) for _ in content_texts]
    for result in wx_results:
        print("TOKENS:", *result["TOKENS"], sep="\n")

    template = model.config["pipeline"]["UD"]["dialog_template"]
    ud_batch = [
        {
            "LANGUAGE": b["LANGUAGE"],
            "SENTENCE": b["SENTENCE"],
            "TOKENS": r["TOKENS"],
        } for b, r in zip(wx_batch, wx_results)
    ]
    print("batch:", *ud_batch, sep="\n")
    ud_contexts = apply_template(template, ud_batch)
    print("context:", *ud_contexts, sep="\n")
    print(*model.dump_prompt_tokens(ud_contexts), sep="\n")
    batch_outputs = model.completion(ud_contexts, model.config["pipeline"]["UD"]["adapter"])
    content_texts = [_.outputs[0].text for _ in batch_outputs]
    print("outputs:", *content_texts, sep="\n")
    ud_results = [parse_output_lines(template["outputs"], _) for _ in content_texts]
    for result in ud_results:
        print("TOKENS:", *result["TOKENS"], sep="\n")


if __name__ == "__main__":
    _test_apply_template()
    _test_parse_output_lines()
    _test_InferenceVLLM()
