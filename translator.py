#!/usr/bin/env python3
"""
Offline Japanese to English Translator
Focuses on translating Kanji characters to English
"""

import json
import os
import sys


class KanjiTranslator:
    """Offline Kanji to English translator"""
    
    def __init__(self, dictionary_path=None):
        """
        Initialize the translator with a Kanji dictionary
        
        Args:
            dictionary_path: Path to the Kanji dictionary JSON file
        """
        if dictionary_path is None:
            # Use default dictionary in the same directory
            dictionary_path = os.path.join(
                os.path.dirname(__file__), 
                'kanji_dict.json'
            )
        
        self.dictionary_path = dictionary_path
        self.kanji_dict = self._load_dictionary()
    
    def _load_dictionary(self):
        """Load the Kanji dictionary from JSON file"""
        try:
            if os.path.exists(self.dictionary_path):
                with open(self.dictionary_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                print(f"Warning: Dictionary file not found at {self.dictionary_path}")
                return {}
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return {}
    
    def translate_kanji(self, kanji_char):
        """
        Translate a single Kanji character to English
        
        Args:
            kanji_char: A single Kanji character
            
        Returns:
            Dictionary with meanings, readings, and examples
        """
        if kanji_char in self.kanji_dict:
            return self.kanji_dict[kanji_char]
        else:
            return None
    
    def translate_text(self, text):
        """
        Translate Japanese text containing Kanji to English
        
        Args:
            text: Japanese text string
            
        Returns:
            List of translations for each Kanji character found
        """
        results = []
        for char in text:
            translation = self.translate_kanji(char)
            if translation:
                results.append({
                    'kanji': char,
                    'translation': translation
                })
        return results
    
    def format_translation(self, translation_data):
        """
        Format translation data for display
        
        Args:
            translation_data: Translation dictionary
            
        Returns:
            Formatted string
        """
        if not translation_data:
            return "Translation not found"
        
        output = []
        output.append(f"Kanji: {translation_data['kanji']}")
        
        trans = translation_data['translation']
        
        if 'meanings' in trans:
            output.append(f"Meanings: {', '.join(trans['meanings'])}")
        
        if 'on_reading' in trans:
            output.append(f"On-reading: {trans['on_reading']}")
        
        if 'kun_reading' in trans:
            output.append(f"Kun-reading: {trans['kun_reading']}")
        
        if 'examples' in trans:
            output.append("Examples:")
            for example in trans['examples']:
                output.append(f"  - {example}")
        
        return '\n'.join(output)


def main():
    """Main function for command-line usage"""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <Japanese text>")
        print("Example: python translator.py 日本")
        sys.exit(1)
    
    japanese_text = sys.argv[1]
    
    # Initialize translator
    translator = KanjiTranslator()
    
    # Translate the text
    results = translator.translate_text(japanese_text)
    
    if not results:
        print("No Kanji characters found or translations available.")
        return
    
    # Display results
    print(f"\nTranslating: {japanese_text}\n")
    print("=" * 50)
    
    for result in results:
        print(translator.format_translation(result))
        print("-" * 50)


if __name__ == "__main__":
    main()
