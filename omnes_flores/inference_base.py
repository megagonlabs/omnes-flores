import json
from abc import ABC, abstractmethod

from transformers import AutoTokenizer

from .dialog_template import apply_template, parse_output_lines
from .utils import print_log


class InferenceBase:

    def __init__(self, main_adapter_name_or_path, args):
        self.tokenizer = AutoTokenizer.from_pretrained(main_adapter_name_or_path)
        self.config = self.tokenizer.init_kwargs["_custom"]["omnes-flores"]

    @abstractmethod
    def completion(self, lora_name_or_path, max_tokens=None, temperature=None):
        pass

    def infer_and_parse(self, component, batch, max_tokens=None, temperature=None):
        component_config = self.config["pipeline"][component]
        template = component_config["dialog_template"]
        contexts = apply_template(template, batch)
        batch_outputs = self.completion(contexts, component_config["adapter"], max_tokens, temperature)
        content_texts = [_.outputs[0].text for _ in batch_outputs]
        results = []
        for job, content_text in zip(batch, content_texts):
            try:
                results.append(parse_output_lines(template["outputs"], content_text))
            except Exception as e:
                print_log(f"skipping: {job}")
        return results

    def analyze_ls(self, text_list: list[str], max_tokens=None, temperature=None):
        if not text_list:
            return []
        total_char = sum(len(_["TEXT"]) for _ in text_list)
        print_log(f"LS: {len(text_list)} target(s), {total_char} total char (TEXT: {text_list[0]["TEXT"][:15]}...)")
        results = self.infer_and_parse("LS", text_list, max_tokens, temperature)
        language_sentence_list = [
            {
                "LANGUAGE": r["LANGUAGE"],
                "SENTENCE": s,
            } for r in results for s in r["SENTENCES"]
        ]
        if language_sentence_list:
            r = language_sentence_list[0]
            snippet = f'LANGUAGE: {r["LANGUAGE"]}, SENTENCE: {r["SENTENCE"][:15]}...'
        else:
            snippet = ""
        print_log(f"LS: retrieved {len(language_sentence_list)} sentences ({snippet})")
        return language_sentence_list

    def analyze_wx(self, language_sentence_list: list[dict], max_tokens=None, temperature=None):
        if not language_sentence_list:
            return []
        r = language_sentence_list[0]
        snippet = f'LANGUAGE: {r["LANGUAGE"]}, SENTENCE: {r["SENTENCE"][:15]}...'
        print_log(f"WX: {len(language_sentence_list)} target(s) ({snippet})")
        results = self.infer_and_parse("WX", language_sentence_list, max_tokens, temperature)
        language_sentence_tokens_list = [
            {
                "LANGUAGE": ls["LANGUAGE"],
                "SENTENCE": ls["SENTENCE"],
                "TOKENS": r["TOKENS"],
            } for ls, r in zip(language_sentence_list, results)
        ]
        if language_sentence_tokens_list:
            r = language_sentence_tokens_list[0]
            snippet = f'LANGUAGE: {r["LANGUAGE"]}, SENTENCE: {r["SENTENCE"][:15]}...]'
        else:
            snippet = ""
        print_log(f"WX: retrieved {len(language_sentence_tokens_list)} sentences ({snippet})")
        return language_sentence_tokens_list

    def analyze_ud(self, language_sentence_tokens_list: list[dict], max_tokens=None, temperature=None):
        if not language_sentence_tokens_list:
            return []
        r = language_sentence_tokens_list[0]
        snippet = f'LANGUAGE: {r["LANGUAGE"]}, SENTENCE: {r["SENTENCE"][:15]}...'
        print_log(f"UD: {len(language_sentence_tokens_list)} target(s) ({snippet})")
        results = self.infer_and_parse("UD", language_sentence_tokens_list, max_tokens, temperature)
        language_sentence_tokens_list = [
            {
                "LANGUAGE": lst["LANGUAGE"],
                "SENTENCE": lst["SENTENCE"],
                "TOKENS": [t1 | t2 for t1, t2 in zip(lst["TOKENS"], r["TOKENS"])],
            } for lst, r in zip(language_sentence_tokens_list, results)
        ]
        if language_sentence_tokens_list:
            r = language_sentence_tokens_list[0]
            snippet = f'LANGUAGE: {r["LANGUAGE"]}, SENTENCE: {r["SENTENCE"][:15]}...]'
        else:
            snippet = ""
        print_log(f"UD: retrieved {len(language_sentence_tokens_list)} sentences ({snippet})")
        return language_sentence_tokens_list

    def analyze_ls_wx(self, text_list: list[str], max_tokens=None, temperature=None):
        language_sentence_list = self.analyze_ls(text_list, max_tokens, temperature)
        return self.analyze_wx(language_sentence_list, max_tokens, temperature)

    def analyze_wx_ud(self, language_sentence_list: list[dict], max_tokens=None, temperature=None):
        language_sentence_tokens_list = self.analyze_wx(language_sentence_list, max_tokens, temperature)
        return self.analyze_ud(language_sentence_tokens_list, max_tokens, temperature)

    def analyze_ls_wx_ud(self, text_list: list[str], max_tokens=None, temperature=None):
        language_sentence_list = self.analyze_ls(text_list, max_tokens, temperature)
        language_sentence_tokens_list = self.analyze_wx(language_sentence_list, max_tokens, temperature)
        return self.analyze_ud(language_sentence_tokens_list, max_tokens, temperature)

    def dump_prompt_tokens(self, batch):
        input_ids_list = self.tokenizer.apply_chat_template(batch)
        dump_texts = []
        for input_ids in input_ids_list:
            dump_text = ""
            for index, id in enumerate(input_ids):
                dump_text += f"{index:7} {json.dumps(self.tokenizer.decode(id), ensure_ascii=False)[1:-1]:32}{id:8}\n"
            dump_texts.append(dump_text)
        return dump_texts
