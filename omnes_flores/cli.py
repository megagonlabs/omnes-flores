import sys
from argparse import ArgumentParser

from .inference_vllm import InferenceVLLM
from .utils import print_log, set_disable_log


def add_args(parser: ArgumentParser = None):
    if parser is None:
        parser = ArgumentParser()
    parser.add_argument("--main_adapter", "--m", default="megagonlabs/omnes-flores-40-lang-41-treebank-v0")
    parser.add_argument("--analyze", "--a", choices=["ls", "ls_wx", "ls_wx_ud"], default="ls_wx_ud")
    parser.add_argument("--output_format", "--f", choices=["conllu"], default="conllu")
    parser.add_argument("--temperature", "--t", type=float, default=0.)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--max_model_len", default=8192, type=int)
    parser.add_argument("--max_tokens", default=8192, type=int)
    parser.add_argument("--gpu_memory_utilization", "--gmu", default=0.85, type=float)
    parser.add_argument("--tensor_parallel_size", "--tp", default=1, type=int)
    parser.add_argument("--num_scheduler_steps", "--ss", default=8, type=int)
    parser.add_argument("--enable_prefix_caching", "--pc", action="store_true")
    parser.add_argument("--enforce_eager", action="store_true")
    parser.add_argument("--quantization", "--q")
    parser.add_argument("--max_lora_rank", "--mlr", default=8, type=int)
    parser.add_argument("--load_format", default="auto")
    parser.add_argument("--max_input_ratio", "--mi", type=float, default=0.25)
    parser.add_argument("--disable_log", "--dl", action="store_true")
    return parser


def main():
    args = add_args().parse_args()
    set_disable_log(args.disable_log)
    print_log(f"loading: {args.main_adapter} ...")
    model = InferenceVLLM(args.main_adapter, args)
    try:
        print_log(f"loaded:  {args.main_adapter}")
        lines = []
        lines_token_len = 0
        while True:
            line = sys.stdin.readline()
            if not line:
                analyze(args.analyze, args.output_format, model, lines, sys.stdout)
                break
            if line.rstrip("\n\r"):
                token_len = len(model.tokenizer.tokenize(line))
                if lines_token_len + token_len < args.max_model_len * args.max_input_ratio:
                    lines.append(line)
                    lines_token_len += token_len
                else:
                    if lines:
                        analyze(args.analyze, args.output_format, model, lines, sys.stdout)
                    if token_len < args.max_model_len * args.max_input_ratio:
                        lines = [line]
                        lines_token_len = token_len
                    else:
                        head_len = int(len(line) / token_len * args.max_model_len * args.max_input_ratio)
                        while line:
                            analyze(args.analyze, args.output_format, model, [line[:head_len]], sys.stdout)
                            line = line[head_len:]
                        lines = []
                        lines_token_len = 0
            else:
                analyze(args.analyze, args.output_format, model, lines, sys.stdout)
                lines = []
                lines_token_len = 0
    except KeyboardInterrupt:
        pass
    finally:
        del model


def analyze(choice, output_format, model, lines, file):
    if choice == "ls":
        results = model.analyze_ls([{"TEXT": "".join(lines)}])
    elif choice == "ls_wx":
        results = model.analyze_ls_wx([{"TEXT": "".join(lines)}])
    elif choice == "ls_wx_ud":
        results = model.analyze_ls_wx_ud([{"TEXT": "".join(lines)}])
    else:
        assert False, f"bad {choice=}"
    if output_format == "conllu":
        for r in results:
            if "LANGUAGE" in r:
                print(f'# language = {r["LANGUAGE"]}', file=file)
            if "SENTENCE" in r:
                print(f'# text = {r["SENTENCE"]}', file=file)
            if "TOKENS" in r:
                for i, t in enumerate(r["TOKENS"], 1):
                    misc = t.get("MISC", [])
                    if i < len(r["TOKENS"]) and not t.get("FORMWS", "").endswith(" "):
                        misc = misc + ["SpaceAfter=No"]
                    print(
                        t.get("ID", "_"),
                        t.get("FORMWS", "_").rstrip(" "),
                        t.get("LEMMA", "_"),
                        t.get("UPOS", "_"),
                        t.get("XPOS", "_"),
                        t.get("FEATS", "_"),
                        t.get("HEAD", "_"),
                        t.get("DEPREL", "_"),
                        t.get("DEPS", "_"),
                        "|".join(misc) if misc else "_",
                        sep="\t",
                        file=file,
                    )
            print(file=file, flush=True)
    else:
        assert False, f"bad {output_format=}"


if __name__ == "__main__":
    main()
