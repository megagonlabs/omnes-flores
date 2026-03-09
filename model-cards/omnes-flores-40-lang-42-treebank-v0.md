---
license: cc-by-sa-4.0
thumbnail: https://github.com/megagonlabs/omnes-flores/raw/main/docs/images/omnes-flores-logo_arc_title.png
datasets:
- universal-dependencies/universal_dependencies
language:
- be
- bor
- cs
- da
- de
- en
- es
- et
- fa
- fi
- fr
- ga
- gd
- he
- hr
- ht
- hy
- hyw
- id
- is
- ja
- ko
- lt
- lv
- nl
- no
- pcm
- pt
- ro
- ru
- sd
- sk
- sl
- sr
- sv
- th
- tr
- uk
- zh
metrics:
- LAS (Labeled Attachment Score)
- UAS (Unlabeled Attachment Score)
- UPOS
- XPOS
- TOKEN
- SENTENCE
base_model:
- google/gemma-2-9b
pipeline_tag: text-generation
library_name: transformers
tags:
- transformers
- vllm
---
# omnes-flores (technology preview)

The [`omnes-flores`](https://megagonlabs.github.io/omnes-flores/) is a unified NLP framework for LLMs consisting of three components:

- The `LS` component takes documents as input, and outputs results of `language identification` and `sentence segmentation` tasks
  - Corresponding model is [omnes-flores-40-lang-42-treebank-v0-ls](https://huggingface.co/megagonlabs/omnes-flores-40-lang-42-treebank-v0-ls).
- The `WX` component takes a sentence and its language, and outputs results of `word segmentation` and `language-specific part-of-speech tagging` tasks
  - Corresponding model is [omnes-flores-40-lang-42-treebank-v0-wx](https://huggingface.co/megagonlabs/omnes-flores-40-lang-42-treebank-v0-wx).
- The `UD` component takes a sentence and its language, constituent word list and language, and outputs results of `dependency parsing` task
  - Corresponding model is on this page.

By executing these three tasks in sequence using the Python library [`omnes-flores`](https://github.com/megagonlabs/omnes-flores), you can obtain dependency parsing results corresponding to the language of the input text simply by inputting text, regardless of the language.

For details, please read the [Requirements](https://github.com/megagonlabs/omnes-flores#requirements) and [Install](https://github.com/megagonlabs/omnes-flores#install) sections in [`omnes-flores` repository](https://github.com/megagonlabs/omnes-flores).

## 42 Treebanks Used for LoRA SFT

This model was trained using training data from 40 UD languages, consisting of 42 treebanks.

This model uses the Corpus of Everyday Japanese Conversation (CEJC) as part of training data, and uses SUW as the Japanese word unit in order to handle non-sentence contexts contained in fragmented speech.  
(本モデルは訓練データの一部に日本語日常会話コーパスを使用しており、日常会話の断片的な発話に含まれる非文法的な文脈に対応するために、日本語の単語分割基準には文節構造を前提としない[国語研短単位](https://clrd.ninjal.ac.jp/bccwj/morphology.html#02)を用いています。)

The following 40 UD treebanks, which have both a commercially available license and over 40k UD tokens in the train set, were select to train the LoRA models of `omnes-flores-40-lang-42-treebank-v0`.

- [UD_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Armenian-ArmTDP),
[UD_Belarusian-HSE](https://github.com/UniversalDependencies/UD_Belarusian-HSE),
[UD_Bororo-BDT](https://github.com/UniversalDependencies/UD_Bororo-BDT),
[UD_Chinese-GSD](https://github.com/UniversalDependencies/UD_Chinese-GSD),
[UD_Chinese-GSDSimp](https://github.com/UniversalDependencies/UD_Chinese-GSDSimp),
[UD_Croatian-SET](https://github.com/UniversalDependencies/UD_Croatian-SET),
[UD_Czech-CAC](https://github.com/UniversalDependencies/UD_Czech-CAC),
[UD_Danish-DDT](https://github.com/UniversalDependencies/UD_Danish-DDT),
[UD_Dutch-Alpino](https://github.com/UniversalDependencies/UD_Dutch-Alpino),
[UD_English-EWT](https://github.com/UniversalDependencies/UD_English-EWT),
[UD_Estonian-EWT](https://github.com/UniversalDependencies/UD_Estonian-EWT),
[UD_Finnish-TDT](https://github.com/UniversalDependencies/UD_Finnish-TDT),
[UD_French-GSD](https://github.com/UniversalDependencies/UD_French-GSD),
[UD_German-GSD](https://github.com/UniversalDependencies/UD_German-GSD),
[UD_Haitian_Creole-Adolphe](https://github.com/UniversalDependencies/UD_Haitian_Creole-Adolphe),
[UD_Hebrew-IAHLTwiki](https://github.com/UniversalDependencies/UD_Hebrew-IAHLTwiki),
[UD_Icelandic-GC](https://github.com/UniversalDependencies/UD_Icelandic-GC),
[UD_Indonesian-GSD](https://github.com/UniversalDependencies/UD_Indonesian-GSD),
[UD_Irish-IDT](https://github.com/UniversalDependencies/UD_Irish-IDT),
[UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW),
[UD_Korean-Kaist](https://github.com/UniversalDependencies/UD_Korean-Kaist),
[UD_Latvian-LVTB](https://github.com/UniversalDependencies/UD_Latvian-LVTB),
[UD_Lithuanian-ALKSNIS](https://github.com/UniversalDependencies/UD_Lithuanian-ALKSNIS),
[UD_Naija-NSC](https://github.com/UniversalDependencies/UD_Naija-NSC),
[UD_Norwegian-Nynorsk](https://github.com/UniversalDependencies/UD_Norwegian-Nynorsk),
[UD_Persian-PerDT](https://github.com/UniversalDependencies/UD_Persian-PerDT),
[UD_Portuguese-Porttinari](https://github.com/UniversalDependencies/UD_Portuguese-Porttinari),
[UD_Romanian-RRT](https://github.com/UniversalDependencies/UD_Romanian-RRT),
[UD_Russian-GSD](https://github.com/UniversalDependencies/UD_Russian-GSD),
[UD_Scottish_Gaelic-ARCOSG](https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG),
[UD_Serbian-SET](https://github.com/UniversalDependencies/UD_Serbian-SET),
[UD_Sindhi-Isra](https://github.com/UniversalDependencies/UD_Sindhi-Isra),
[UD_Slovak-SNK](https://github.com/UniversalDependencies/UD_Slovak-SNK),
[UD_Slovenian-SSJ](https://github.com/UniversalDependencies/UD_Slovenian-SSJ),
[UD_Spanish-GSD](https://github.com/UniversalDependencies/UD_Spanish-GSD),
[UD_Swedish-Talbanken](https://github.com/UniversalDependencies/UD_Swedish-Talbanken),
[UD_Thai-TUD](https://github.com/UniversalDependencies/UD_Thai-TUD),
[UD_Turkish-BOUN](https://github.com/UniversalDependencies/UD_Turkish-BOUN),
[UD_Ukrainian-ParlaMint](https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint),
[UD_Western_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP),

In addition, the following datasets were used for training, which were specially licensed from the [National Institute for Japanese Language and Linguistics](https://www.ninjal.ac.jp/english/) exclusively for training this model.

- [UD_Japanese-BCCWJ](https://github.com/UniversalDependencies/UD_Japanese-BCCWJ) (excluding PN newspaper articles)
- [UD_Japanese-CEJC](https://github.com/UniversalDependencies/UD_Japanese-CEJC)

## Acknowledgements

This work was conducted as part of a collaborative research project between Recruit Co., Ltd. and the [National Institute for Japanese Language and Linguistics](https://www.ninjal.ac.jp/english/).

## Citations

You are encouraged to cite one of the following papers if you use omnes-flores models:

```bibtex
@inproceedings{matsuda-etal-2025-step,
    title = "Step-by-step Instructions and a Simple Tabular Output Format Improve the Dependency Parsing Accuracy of {LLM}s",
    author = "Matsuda, Hiroshi  and
      Ma, Chunpeng  and
      Asahara, Masayuki",
    editor = "Sagae, Kenji  and
      Oepen, Stephan",
    booktitle = "Proceedings of the 18th International Conference on Parsing Technologies (IWPT, SyntaxFest 2025)",
    month = aug,
    year = "2025",
    address = "Ljubljana, Slovenia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.iwpt-1.2/",
    pages = "11--19",
    ISBN = "979-8-89176-294-7",
    abstract = "Recent advances in large language models (LLMs) have enabled impressive performance in various tasks. However, standard prompting often struggles to produce structurally valid and accurate outputs, especially in dependency parsing. We propose a novel step-by-step instruction strategy, where universal part-of-speech tagging precedes the prediction of syntactic heads and dependency labels, and a simplified CoNLL-U like output format, our method achieves state-of-the-art accuracy on Universal Dependencies datasets across 17 languages without hallucination or contamination. We further show that multilingual fine-tuning simultaneously improves cross-language generalization performance. Our results highlight the effectiveness of explicit reasoning steps in LLM-based parsing and offer a scalable, format-consistent alternative to bracket-based approaches."
}

@misc{matsuda2025stepbystepinstructionssimpletabular,
      title={Step-by-step Instructions and a Simple Tabular Output Format Improve the Dependency Parsing Accuracy of LLMs}, 
      author={Hiroshi Matsuda and Chunpeng Ma and Masayuki Asahara},
      year={2025},
      eprint={2506.09983},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.09983}, 
}
```
