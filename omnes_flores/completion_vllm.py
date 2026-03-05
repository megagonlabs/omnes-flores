from argparse import ArgumentParser

from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest


class CompletionVLLM:
    model: LLM
    lora_requests: list[LoRARequest]
    sampling_params: SamplingParams

    def __init__(self, model_name_or_path, tokenizer_name_or_path, args):
        print(f"loading model:{model_name_or_path} and tokenizer:{tokenizer_name_or_path} ...")
        self.model = LLM(
            model=model_name_or_path,
            tokenizer=tokenizer_name_or_path,
            enable_lora=True,
            dtype=args.dtype,
            max_model_len=args.max_model_len,
            gpu_memory_utilization=args.gpu_memory_utilization,
            tensor_parallel_size=args.tensor_parallel_size,
            enforce_eager=args.enforce_eager,
            quantization=args.quantization,
            max_lora_rank=args.max_lora_rank,
            load_format=args.load_format,
        )
        print(f" loaded model:{model_name_or_path} and tokenizer:{tokenizer_name_or_path}")
        self.temperature = args.temperature or 0.0

    def __del__(self):
        if "model" in dir(self):
            self.model.llm_engine.engine_core.shutdown()
            try:
                del self.model
            except Exception as e:
                print(f"Failed to unload model: {e}")

    def add_lora(self, lora_path):
        self.lora_requests[lora_path] = LoRARequest(lora_path, 1, lora_path)

    def completion(self, batch, lora_path, max_tokens=None, temperature=None):
        self.sampling_params = SamplingParams(
            max_tokens=max_tokens if max_tokens is not None else self.llm.max_model_len,
            temperature=temperature if temperature is not None else self.temperature
        )
        outputs = self.model.chat(
            messages=batch,
            lora_request=self.lora_requests[lora_path],
            sampling_params=self.sampling_params,
            use_tqdm=False,
        )
        return outputs


def _test():
    import tomllib
    from .message import apply_template
    from .parse_output import parse_output_lines
    from .cli import add_args

    with open("omnes_flores/resources/40-lang-41-treebank.toml", "rb") as fin:
        config = tomllib.load(fin)
    model = CompletionVLLM(config["base"]["model"], config["base"]["tokenizer"], add_args().parse_args())

    template = config["ls"]["dialog_template"]
    batch = apply_template(template, [{"text": "This is a test text document."}])
    print(batch)
    outputs = model.completion(batch)
    print(outputs)
    results = parse_output_lines(template["outputs"], outputs)
    print(results)

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
