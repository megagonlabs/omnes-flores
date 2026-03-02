from argparse import ArgumentParser

from vllm import LLM, SamplingParams
from vllm.entrypoints.chat_utils import (apply_hf_chat_template,
                                         apply_mistral_chat_template,
                                         parse_chat_messages,
                                         resolve_chat_template_content_format)
from vllm.lora.request import LoRARequest
from vllm.transformers_utils.tokenizer import MistralTokenizer
from vllm.v1.engine.llm_engine import LLMEngine as LLMEngineV1


def main():
    parser = ArgumentParser()
    parser.add_argument("--model_name_or_path", "--m", type=str, default="google/gemma-2-9b")
    parser.add_argument("--adapter_name_or_path", "--a", type=str, default="megagonlabs/omnes-flores-40-lang-41-treebank-v0-ud")
    parser.add_argument("--input_text", "--it", type=str)
    parser.add_argument("--input_sentence", "--is", type=str)
    parser.add_argument("--input_language", "--il", type=str)
    parser.add_argument("--output_conllu", "--o", type=str)
    parser.add_argument("--temperature", "--t", type=float, default=0.)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--max_model_len", default=4096, type=int)
    parser.add_argument("--gpu_memory_utilization", "--gmu", default=0.9, type=float)
    parser.add_argument("--tensor_parallel_size", "--tp", default=1, type=int)
    parser.add_argument("--num_scheduler_steps", "--ss", default=8, type=int)
    parser.add_argument("--enable_prefix_caching", "--pc", action="store_true")
    parser.add_argument("--enforce_eager", action="store_true")
    parser.add_argument("--quantization", "--q")
    parser.add_argument("--max_lora_rank", "--mlr", default=8, type=int)
    parser.add_argument("--load_format", default="auto")
    args = parser.parse_args()
    vllm_main(args)


def vllm_main(args):
    print(f"loading model: {args}")
    llm = LLM(
        model=args.model_name_or_path,
        enable_lora=args.adapter_name_or_path is not None,
        tokenizer=args.model_name_or_path,
        dtype=args.dtype,
        max_model_len=args.max_model_len,
        gpu_memory_utilization=args.gpu_memory_utilization,
        tensor_parallel_size=args.tensor_parallel_size,
        enforce_eager=args.enforce_eager,
        quantization=args.quantization,
        max_lora_rank=args.max_lora_rank,
        load_format=args.load_format,
    )
    print(f"model loaded")
    """
    tokenizer = llm.get_tokenizer()
    lora_request = LoRARequest("adapter", 1, args.adapter_name_or_path)
    sampling_params = SamplingParams(
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    results = llm.chat(
        messages=[full_messages[:chat_index] for line_index, chat_index, full_messages in batch],
        sampling_params=sampling_params,
        use_tqdm=False,
        lora_request=lora_request,
    )
    m = full_messages[chat_index]
    m["gold"] = m["content"]
    content_text = result.outputs[0].text
    m["content"] = content_text
    if is_first:
        is_first = False
        logger.debug(f"\n====== line #{line_index} - {chat_index} ======")
        logger.debug("\n" + full_messages[chat_index - 1]["content"])
        logger.debug("\n" + content_text)
    print()
    """


if __name__ == "__main__":
    main()
