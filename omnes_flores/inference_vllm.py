import json
import os
import sys
from pathlib import Path

if os.getenv("VLLM_CONFIGURE_LOGGING") is None and os.getenv("VLLM_LOGGING_CONFIG_PATH") is None:
    vllm_logging_config_path = f"{Path(__file__).parent}/vllm_logging_config.json"
    os.environ["VLLM_LOGGING_CONFIG_PATH"] = vllm_logging_config_path
    print(f"\033[46mVLLM_LOGGING_CONFIG_PATH={vllm_logging_config_path}\033[0m", file=sys.stderr)

from transformers import PreTrainedTokenizerBase
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest

from .inference_base import InferenceBase
from .utils import print_log


class InferenceVLLM(InferenceBase):
    llm: LLM
    lora_requests: list[LoRARequest]
    sampling_params: SamplingParams

    def __init__(self, main_adapter_name_or_path, args):
        super().__init__(main_adapter_name_or_path, args)
        self.llm = LLM(
            model=self.config["base"]["model"],
            tokenizer=self.config["base"]["tokenizer"],
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
        self.max_tokens = args.max_tokens
        self.temperature = args.temperature
        self.lora_requests = {}
        for v in self.config["pipeline"].values():
            self.load_lora(v["adapter"])

    def __del__(self):
        if "llm" in dir(self):
            self.llm.llm_engine.engine_core.shutdown()
            try:
                del self.llm
            except Exception as e:
                print_log(f"Failed to unload self.llm: {e}")

    def completion(self, batch, lora_name_or_path, max_tokens=None, temperature=None):
        lora_request = self.load_lora(lora_name_or_path)
        self.sampling_params = SamplingParams(
            max_tokens=max_tokens if max_tokens is not None else self.max_tokens,
            temperature=temperature if temperature is not None else self.temperature
        )
        outputs = self.llm.chat(
            messages=batch,
            lora_request=lora_request,
            sampling_params=self.sampling_params,
            use_tqdm=False,
        )
        return outputs

    def load_lora(self, lora_name_or_path):
        if lora_name_or_path in self.lora_requests:
            return self.lora_requests[lora_name_or_path]
        new_lora_request = LoRARequest(lora_name_or_path, len(self.lora_requests) + 1, lora_name_or_path)
        self.lora_requests[lora_name_or_path] = new_lora_request
        print_log(f"LoRARequest #{len(self.lora_requests)}: {lora_name_or_path}")
        return new_lora_request
