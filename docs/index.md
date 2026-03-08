# omnes-flores Technology Preview

**A Unified NLP Framework for LLMs.**

[![Downloads](https://pepy.tech/badge/omnes-flores/week)](https://pepy.tech/project/omnes-flores)

## Terms of Use

The `omnes-flores` Python module is published under [Apache License Version 2.0](./LICENSE) and the dedicated models for `omnes-flores` are distributed under the license inherited from the Universal Dependencies treebanks used for training.

To use the base model [`google/gemma-2-9b`](https://huggingface.co/google/gemma-2-9b), you must agree to the terms of use in your HuggingFace account.

> To access Gemma on Hugging Face, you’re required to review and agree to Google’s usage license. To do this, please ensure you’re logged in to Hugging Face and click below. Requests are processed immediately.

## Requirements

The `omnes-flores` technology preview requires a Linux environment with NVIDIA GPUs (Ampere or later).
To run inference on the 9B parameter base model + LoRA using `bfloat16`, 24GB or more of GPU memory is required.
The following environments have been tested for operation.

- NVIDIA RTX Pro 6000 Blackwell 96GB
- CPU RAM 64GB
- Ubuntu 24.04
- CUDA 12.8
- Python 3.12
- vLLM 0.16.0
- Transformers 4.57.6

We are planning to support Apple Silicon (MLX) in the near future.

## Install

Installing the library is very simple like:

```Console
$ pip install omnes-flores
```

## Models

### `40-lang-41-treebank-v0` (CC BY-SA 4.0)

```Console
$ omnes-flores < text_file > conllu_file
```

This model is available for commercial use.

This model was trained using training data from 40 UD languages, consisting of 41 treebanks.

The Japanese word unit is LUW.  
(日本語の単語分割基準は[国語研長単位](https://clrd.ninjal.ac.jp/bccwj/morphology.html#06)です。)

The following 40 UD treebanks, which have both a commercially available license and over 40k UD tokens in the train set, were select to train the LoRA models of `omnes-flores-40-lang-41-treebank-v0`.

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

In addition, a proprietary treebank was used for training, which were specially licensed from the [National Institute for Japanese Language and Linguistics](https://www.ninjal.ac.jp/english/) exclusively for training this model.

- [UD_Japanese-BCCWJLUW](https://github.com/UniversalDependencies/UD_Japanese-BCCWJLUW) (excluding PN newspaper articles)

### `40-lang-42-treebank-v0` (CC BY-SA 4.0)

```Console
$ omnes-flores --m megagonlabs/omnes-flores-40-lang-42-treebank-v0 < text_file > conllu_file
```

This model is available for commercial use.

This model uses the `Corpus of Everyday Japanese Conversation` (CEJC) as part of training data, and uses SUW as the Japanese word unit in order to handle non-sentence contexts contained in fragmented speech.  
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

### `84-lang-99-treebank-non-commercial-v0` (CC BY-NC-SA 4.0)

```Console
$ omnes-flores --m megagonlabs/omnes-flores-84-lang-99-treebank-non-commercial-v0 < text_file > conllu_file
```

This model is made available for non-commercial use, including academic use; commercial use is strictly prohibited.

The Japanese word unit is LUW.  
(日本語の単語分割基準は[国語研長単位](https://clrd.ninjal.ac.jp/bccwj/morphology.html#06)です。)

The following 40 UD treebanks, which have both a commercially available license and over 40k UD tokens in the train set, were select to train the LoRA models of `omnes-flores-84-lang-99-treebank-non-commercial-v0`.

- [UD_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Armenian-ArmTDP)
[UD_Belarusian-HSE](https://github.com/UniversalDependencies/UD_Belarusian-HSE)
[UD_Bororo-BDT](https://github.com/UniversalDependencies/UD_Bororo-BDT)
[UD_Chinese-GSD](https://github.com/UniversalDependencies/UD_Chinese-GSD)
[UD_Chinese-GSDSimp](https://github.com/UniversalDependencies/UD_Chinese-GSDSimp)
[UD_Croatian-SET](https://github.com/UniversalDependencies/UD_Croatian-SET)
[UD_Czech-CAC](https://github.com/UniversalDependencies/UD_Czech-CAC)
[UD_Danish-DDT](https://github.com/UniversalDependencies/UD_Danish-DDT)
[UD_Dutch-Alpino](https://github.com/UniversalDependencies/UD_Dutch-Alpino)
[UD_English-EWT](https://github.com/UniversalDependencies/UD_English-EWT)
[UD_Estonian-EWT](https://github.com/UniversalDependencies/UD_Estonian-EWT)
[UD_Finnish-TDT](https://github.com/UniversalDependencies/UD_Finnish-TDT)
[UD_French-GSD](https://github.com/UniversalDependencies/UD_French-GSD)
[UD_German-GSD](https://github.com/UniversalDependencies/UD_German-GSD)
[UD_Haitian_Creole-Adolphe](https://github.com/UniversalDependencies/UD_Haitian_Creole-Adolphe)
[UD_Hebrew-IAHLTwiki](https://github.com/UniversalDependencies/UD_Hebrew-IAHLTwiki)
[UD_Icelandic-GC](https://github.com/UniversalDependencies/UD_Icelandic-GC)
[UD_Indonesian-GSD](https://github.com/UniversalDependencies/UD_Indonesian-GSD)
[UD_Irish-IDT](https://github.com/UniversalDependencies/UD_Irish-IDT)
[UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW)
[UD_Korean-Kaist](https://github.com/UniversalDependencies/UD_Korean-Kaist)
[UD_Latvian-LVTB](https://github.com/UniversalDependencies/UD_Latvian-LVTB)
[UD_Lithuanian-ALKSNIS](https://github.com/UniversalDependencies/UD_Lithuanian-ALKSNIS)
[UD_Naija-NSC](https://github.com/UniversalDependencies/UD_Naija-NSC)
[UD_Norwegian-Nynorsk](https://github.com/UniversalDependencies/UD_Norwegian-Nynorsk)
[UD_Persian-PerDT](https://github.com/UniversalDependencies/UD_Persian-PerDT)
[UD_Portuguese-Porttinari](https://github.com/UniversalDependencies/UD_Portuguese-Porttinari)
[UD_Romanian-RRT](https://github.com/UniversalDependencies/UD_Romanian-RRT)
[UD_Russian-GSD](https://github.com/UniversalDependencies/UD_Russian-GSD)
[UD_Scottish_Gaelic-ARCOSG](https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG)
[UD_Serbian-SET](https://github.com/UniversalDependencies/UD_Serbian-SET)
[UD_Sindhi-Isra](https://github.com/UniversalDependencies/UD_Sindhi-Isra)
[UD_Slovak-SNK](https://github.com/UniversalDependencies/UD_Slovak-SNK)
[UD_Slovenian-SSJ](https://github.com/UniversalDependencies/UD_Slovenian-SSJ)
[UD_Spanish-GSD](https://github.com/UniversalDependencies/UD_Spanish-GSD)
[UD_Swedish-Talbanken](https://github.com/UniversalDependencies/UD_Swedish-Talbanken)
[UD_Thai-TUD](https://github.com/UniversalDependencies/UD_Thai-TUD)
[UD_Turkish-BOUN](https://github.com/UniversalDependencies/UD_Turkish-BOUN)
[UD_Ukrainian-ParlaMint](https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint)
[UD_Western_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP)

In addition, the following 59 treebanks have been added to the training in this model for academic purposes:

- [UD_Ancient_Greek-PTNK](https://github.com/UniversalDependencies/UD_Ancient_Greek-PTNK)
[UD_Ancient_Greek-PROIEL](https://github.com/UniversalDependencies/UD_Ancient_Greek-PROIEL)
[UD_Ancient_Greek-Perseus](https://github.com/UniversalDependencies/UD_Ancient_Greek-Perseus)
[UD_Ancient_Hebrew-PTNK](https://github.com/UniversalDependencies/UD_Ancient_Hebrew-PTNK)
[UD_Basque-BDT](https://github.com/UniversalDependencies/UD_Basque-BDT)
[UD_Bulgarian-BTB](https://github.com/UniversalDependencies/UD_Bulgarian-BTB)
[UD_Classical_Armenian-CAVaL](https://github.com/UniversalDependencies/UD_Classical_Armenian-CAVaL)
[UD_Classical_Chinese-Kyoto](https://github.com/UniversalDependencies/UD_Classical_Chinese-Kyoto)
[UD_Coptic-Scriptorium](https://github.com/UniversalDependencies/UD_Coptic-Scriptorium)
[UD_Coptic-Bohairic](https://github.com/UniversalDependencies/UD_Coptic-Bohairic)
[UD_Egyptian-PC](https://github.com/UniversalDependencies/UD_Egyptian-PC)
[UD_Erzya-JR](https://github.com/UniversalDependencies/UD_Erzya-JR)
[UD_Estonian-EDT](https://github.com/UniversalDependencies/UD_Estonian-EDT)
[UD_Galician-CTG](https://github.com/UniversalDependencies/UD_Galician-CTG)
[UD_Galician-TreeGal](https://github.com/UniversalDependencies/UD_Galician-TreeGal)
[UD_Georgian-GLC](https://github.com/UniversalDependencies/UD_Georgian-GLC)
[UD_Gothic-PROIEL](https://github.com/UniversalDependencies/UD_Gothic-PROIEL)
[UD_Greek-GDT](https://github.com/UniversalDependencies/UD_Greek-GDT)
[UD_Hindi-HDTB](https://github.com/UniversalDependencies/UD_Hindi-HDTB)
[UD_Hungarian-Szeged](https://github.com/UniversalDependencies/UD_Hungarian-Szeged)
[UD_Icelandic-IcePaHC](https://github.com/UniversalDependencies/UD_Icelandic-IcePaHC)
[UD_Icelandic-Modern](https://github.com/UniversalDependencies/UD_Icelandic-Modern)
[UD_Italian-ISDT](https://github.com/UniversalDependencies/UD_Italian-ISDT)
[UD_Italian-Old](https://github.com/UniversalDependencies/UD_Italian-Old)
[UD_Khoekhoe-KDT](https://github.com/UniversalDependencies/UD_Khoekhoe-KDT)
[UD_Kyrgyz-KTMU](https://github.com/UniversalDependencies/UD_Kyrgyz-KTMU)
[UD_Latin-CIRCSE](https://github.com/UniversalDependencies/UD_Latin-CIRCSE)
[UD_Latin-ITTB](https://github.com/UniversalDependencies/UD_Latin-ITTB)
[UD_Latin-LLCT](https://github.com/UniversalDependencies/UD_Latin-LLCT)
[UD_Latin-Perseus](https://github.com/UniversalDependencies/UD_Latin-Perseus)
[UD_Latin-PROIEL](https://github.com/UniversalDependencies/UD_Latin-PROIEL)
[UD_Latin-UDante](https://github.com/UniversalDependencies/UD_Latin-UDante)
[UD_Low_Saxon-LSDC](https://github.com/UniversalDependencies/UD_Low_Saxon-LSDC)
[UD_Maltese-MUDT](https://github.com/UniversalDependencies/UD_Maltese-MUDT)
[UD_Manx-Cadhan](https://github.com/UniversalDependencies/UD_Manx-Cadhan)
[UD_Middle_French-PROFITEROLE](https://github.com/UniversalDependencies/UD_Middle_French-PROFITEROLE)
[UD_Nheengatu-CompLin](https://github.com/UniversalDependencies/UD_Nheengatu-CompLin)
[UD_North_Sami-Giella](https://github.com/UniversalDependencies/UD_North_Sami-Giella)
[UD_Occitan-TTB](https://github.com/UniversalDependencies/UD_Occitan-TTB)
[UD_Old_Church_Slavonic-PROIEL](https://github.com/UniversalDependencies/UD_Old_Church_Slavonic-PROIEL)
[UD_Old_East_Slavic-RNC](https://github.com/UniversalDependencies/UD_Old_East_Slavic-RNC)
[UD_Old_East_Slavic-Ruthenian](https://github.com/UniversalDependencies/UD_Old_East_Slavic-Ruthenian)
[UD_Old_East_Slavic-TOROT](https://github.com/UniversalDependencies/UD_Old_East_Slavic-TOROT)
[UD_Old_East_Slavic-Birchbark](https://github.com/UniversalDependencies/UD_Old_East_Slavic-Birchbark)
[UD_Old_French-PROFITEROLE](https://github.com/UniversalDependencies/UD_Old_French-PROFITEROLE)
[UD_Old_Occitan-CorAG](https://github.com/UniversalDependencies/UD_Old_Occitan-CorAG)
[UD_Ottoman_Turkish-DUDU](https://github.com/UniversalDependencies/UD_Ottoman_Turkish-DUDU)
[UD_Ottoman_Turkish-BOUN](https://github.com/UniversalDependencies/UD_Ottoman_Turkish-BOUN)
[UD_Polish-MPDT](https://github.com/UniversalDependencies/UD_Polish-MPDT)
[UD_Pomak-Philotis](https://github.com/UniversalDependencies/UD_Pomak-Philotis)
[UD_Sanskrit-Vedic](https://github.com/UniversalDependencies/UD_Sanskrit-Vedic)
[UD_Sindhi-Isra](https://github.com/UniversalDependencies/UD_Sindhi-Isra)
[UD_Urdu-UDTB](https://github.com/UniversalDependencies/UD_Urdu-UDTB)
[UD_Uyghur-UDT](https://github.com/UniversalDependencies/UD_Uyghur-UDT)
[UD_Vietnamese-VTB](https://github.com/UniversalDependencies/UD_Vietnamese-VTB)
[UD_Welsh-CCG](https://github.com/UniversalDependencies/UD_Welsh-CCG)
[UD_Wolof-WTB](https://github.com/UniversalDependencies/UD_Wolof-WTB)
[UD_Yiddish-YiTB](https://github.com/UniversalDependencies/UD_Yiddish-YiTB)
[UD_Zaar-Autogramm](https://github.com/UniversalDependencies/UD_Zaar-Autogramm)

## Method

The analysis pipeline components use following prompts:

<img src="./images/prompt_ls.png" style="width: 75%; height: auto;">

Figure 1: An example of `language identification` and `sentence segmentation` prompt instance. The parts that change from instance to instance are shown in _Italic_. The SHADED REGION in the assistant-role corresponds to the range over which the loss gradient is computed during training, and to the decoded text during inference. At inference time, the span from the system-role up to the assistant-role header is provided as input, and decoding of the subsequent segment continues until `<eos>` is generated.

<img src="./images/prompt_wx.png" style="width: 75%; height: auto;">

Figure 2: An example of `word segmentation` and `language-specific part-of-speech tagging` prompt instance.

<img src="./images/prompt_ud.png" style="width: 75%; height: auto;">

Figure 3: An example of `dependency parsing` prompt instance.

### Evaluation Result

[![omnes-flores-40-lang-41-treebank-v0-eval.png](./images/omnes-flores-40-lang-41-treebank-v0-eval.png)](./images/omnes-flores-40-lang-41-treebank-v0-eval.png)

Figure 4: Accuracy of the proposed method and UDPipe2 on 41 treebanks (average of 4 trials ± sample standard deviation). Yellow highlights indicate relatively small training data or relatively low accuracy. Green highlights indicate relatively large sample standard deviation.

Read the [NLP2026 paper (多言語統語解析処理のためのMulti-task LoRA SFT方式の評価)](https://github.com/megagonlabs/omnes-flores/raw/main/docs/images/NLP2026_TS2-16_paper.pdf) and its [poster material](https://github.com/megagonlabs/omnes-flores/raw/main/docs/images/NLP2026_TS2-16_poster.pdf) (written in Japanese) for details.

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

## [Version History](https://github.com/megagonlabs/omnes-flores/releases)

### 0.1.0-alpha
- 2026-03-09 Release 0.1.0a
