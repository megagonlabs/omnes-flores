from argparse import ArgumentParser


def add_args(parser=None):
    if parser is None:
        parser = ArgumentParser()
    parser.add_argument("--temperature", "--t", type=float, default=0.)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--max_model_len", default=8192, type=int)
    parser.add_argument("--gpu_memory_utilization", "--gmu", default=0.85, type=float)
    parser.add_argument("--tensor_parallel_size", "--tp", default=2, type=int)
    parser.add_argument("--num_scheduler_steps", "--ss", default=8, type=int)
    parser.add_argument("--enable_prefix_caching", "--pc", action="store_true")
    parser.add_argument("--enforce_eager", action="store_true")
    parser.add_argument("--quantization", "--q")
    parser.add_argument("--max_lora_rank", "--mlr", default=8, type=int)
    parser.add_argument("--load_format", default="auto")
    return parser


def main():
    args = add_args()


if __name__ == "__main__":
    main()
