#!/usr/bin/env python3
"""
Example usage script for the Japanese to English Kanji translator
"""

from translator import KanjiTranslator


def main():
    print("=" * 70)
    print("Japanese to English Translator - Example Usage")
    print("=" * 70)
    
    # Initialize the translator
    translator = KanjiTranslator()
    
    # Example 1: Translate common words
    print("\n1. Translating common Japanese words:\n")
    
    words = ['日本', '日本語', '英語', '学校', '先生']
    
    for word in words:
        print(f"\n📖 Word: {word}")
        print("-" * 40)
        results = translator.translate_text(word)
        
        if results:
            for result in results:
                trans = result['translation']
                meanings = ', '.join(trans['meanings'])
                print(f"  {result['kanji']}: {meanings}")
        else:
            print("  No translations found")
    
    # Example 2: Detailed translation of a single Kanji
    print("\n\n2. Detailed translation of a single Kanji:\n")
    print("=" * 70)
    
    kanji = '心'
    result = translator.translate_kanji(kanji)
    if result:
        formatted = translator.format_translation({
            'kanji': kanji,
            'translation': result
        })
        print(formatted)
    
    # Example 3: Days of the week
    print("\n\n3. Days of the week (Kanji):\n")
    print("=" * 70)
    
    days = {
        '月曜日': 'Monday',
        '火曜日': 'Tuesday',
        '水曜日': 'Wednesday',
        '木曜日': 'Thursday',
        '金曜日': 'Friday',
        '土曜日': 'Saturday',
    }
    
    for day_kanji, day_english in days.items():
        print(f"\n{day_kanji} ({day_english}):")
        results = translator.translate_text(day_kanji)
        for result in results:
            trans = result['translation']
            meanings = trans['meanings'][0] if trans['meanings'] else 'N/A'
            print(f"  {result['kanji']}: {meanings}")
    
    # Example 4: Nature words
    print("\n\n4. Nature-related Kanji:\n")
    print("=" * 70)
    
    nature_kanji = ['山', '川', '水', '火', '木', '花']
    
    print("\nNature elements:")
    for kanji in nature_kanji:
        result = translator.translate_kanji(kanji)
        if result:
            meanings = ', '.join(result['meanings'])
            print(f"  {kanji} → {meanings}")
    
    # Example 5: Family words
    print("\n\n5. Family-related Kanji:\n")
    print("=" * 70)
    
    family = ['父', '母', '子', '友']
    
    print("\nFamily members:")
    for kanji in family:
        result = translator.translate_kanji(kanji)
        if result:
            meanings = ', '.join(result['meanings'])
            kun = result.get('kun_reading', 'N/A')
            print(f"  {kanji} → {meanings} (kun: {kun})")
    
    print("\n" + "=" * 70)
    print("End of examples")
    print("=" * 70)
    print("\nTry it yourself:")
    print("  python translator.py 日本")
    print("  python translator.py 学校")
    print("  python translator.py あなたの好きな漢字")
    print("=" * 70)


if __name__ == "__main__":
    main()
