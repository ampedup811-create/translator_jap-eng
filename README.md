# Japanese to English Translator (Offline)

An offline Japanese to English translator focusing on Kanji character translation. This tool works completely offline without requiring an internet connection, making it perfect for quick Kanji lookups.

## Features

- **Offline Translation**: Works without internet connection
- **Kanji Focus**: Specialized dictionary for common Kanji characters
- **Detailed Information**: Provides meanings, readings (On-reading and Kun-reading), and usage examples
- **Simple CLI**: Easy-to-use command-line interface
- **No External Dependencies**: Uses only Python standard library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ampedup811-create/translator_jap-eng.git
cd translator_jap-eng
```

2. Ensure you have Python 3.6 or higher installed:
```bash
python --version
```

No additional dependencies are required!

## Usage

### Command Line Interface

Translate Japanese text containing Kanji:

```bash
python translator.py 日本
```

Example output:
```
Translating: 日本

==================================================
Kanji: 日
Meanings: sun, day
On-reading: ニチ、ジツ (nichi, jitsu)
Kun-reading: ひ、か (hi, ka)
Examples:
  - 日本 (にほん/にっぽん) - Japan
  - 毎日 (まいにち) - every day
  - 今日 (きょう) - today
--------------------------------------------------
Kanji: 本
Meanings: book, origin, main, true
On-reading: ホン (hon)
Kun-reading: もと (moto)
Examples:
  - 日本 (にほん) - Japan
  - 本屋 (ほんや) - bookstore
  - 絵本 (えほん) - picture book
--------------------------------------------------
```

### More Examples

Translate "学校" (school):
```bash
python translator.py 学校
```

Translate "日本語" (Japanese language):
```bash
python translator.py 日本語
```

### As a Python Module

You can also use the translator in your Python scripts:

```python
from translator import KanjiTranslator

# Initialize the translator
translator = KanjiTranslator()

# Translate a single Kanji
result = translator.translate_kanji('日')
print(result)

# Translate text containing multiple Kanji
results = translator.translate_text('日本語')
for result in results:
    print(translator.format_translation(result))
```

## Dictionary Coverage

The included dictionary contains 42 common Kanji characters covering:
- Basic elements (日, 月, 火, 水, 木, 金, 土)
- Common words (人, 本, 国, 学, 校, 生, 先)
- Nature (山, 川, 花)
- Body parts (手, 足, 目, 口, 心)
- Family (父, 母, 子, 友)
- Actions (食, 飲)
- Descriptors (大, 小, 新, 古, 高, 安)
- And more!

## Extending the Dictionary

To add more Kanji to the dictionary, edit the `kanji_dict.json` file:

```json
{
  "漢": {
    "meanings": ["China", "Han", "Chinese"],
    "on_reading": "カン (kan)",
    "kun_reading": "",
    "examples": [
      "漢字 (かんじ) - Kanji",
      "漢文 (かんぶん) - Chinese classics"
    ]
  }
}
```

## Project Structure

```
translator_jap-eng/
├── translator.py       # Main translator module and CLI
├── kanji_dict.json    # Kanji dictionary database
├── requirements.txt   # Python dependencies (none required)
└── README.md         # This file
```

## Technical Details

- **Language**: Python 3.6+
- **Storage Format**: JSON for easy editing and expansion
- **Character Encoding**: UTF-8 for proper Japanese character handling
- **Dependencies**: None (uses only Python standard library)

## Limitations

- Currently focuses on individual Kanji characters
- Dictionary contains 42 common Kanji (easily expandable)
- Does not handle full sentence translation or grammar
- Does not include Hiragana/Katakana-only words

## Future Enhancements

Potential improvements for future versions:
- Expanded dictionary with more Kanji
- Compound word recognition
- Hiragana and Katakana support
- Sentence-level translation
- Web interface
- Mobile app version

## Contributing

Contributions are welcome! To add more Kanji to the dictionary:
1. Fork the repository
2. Add entries to `kanji_dict.json`
3. Test your additions
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Author

Created for offline Japanese learning and quick Kanji reference.
