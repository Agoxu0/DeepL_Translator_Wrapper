# DEEPL_Translator

DEEPL_Translator is a Python library that provides a simple interface for translating text using DeepL, a popular machine translation service. It supports translation between various languages.

## Installation

You can install DEEPL_Translator using pip:

```bash
pip install git+https://github.com/Agoxu0/DeepL_Translator_Wrapper
```

# Basic Usage
To use DeepL_Translator, follow these simple steps:
1. Import the DeepL_Translator class:
```python
from DeepL_Translator import Translator
```
2. Create an instance of the DEEPL_Translator class:
```python
DeepL = Translator()
```
3. Translate text using the Translate method:
```python
text = "Hi!"
target_language = "pl"  # Replace with the target language code from the list below
translated_text = DeepL.Translate(text, target_language)
print(translated_text)
```
4. Replace "fr" with the language code of the target language you want to translate to. You can choose from the following list of language codes:
```
Bulgarian
"bg",
Chinese(simplified)
"zh",
Czech
"cs",
Danish
"da",
Dutch
"nl",
English(American)
"en-US",
English(British)
"en-GB",
Estonian
"et",
Finnish
"fi",
French
"fr",
German
"de",
Greek
"el",
Hungarian
"hu",
Indonesian
"id",
Italian
"it",
Japanese
"ja",
Korean
"ko",
Latvian
"lv",
Lithuanian
"lt",
Norwegian(bokmål)
"nb",
Polish
"pl",
Portuguese
"pt-PT",
Portuguese(Brazilian)
"pt-BR",
Romanian
"ro",
Russian
"ru",
Slovak
"sk",
Slovenian
"sl",
Spanish
"es",
Swedish
"sv",
Turkish
"tr",
Ukrainian
"uk"
```
