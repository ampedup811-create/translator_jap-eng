#!/usr/bin/env python3
"""
Test script for the Kanji translator
"""

from translator import KanjiTranslator


def test_basic_translation():
    """Test basic translation functionality"""
    print("Testing basic Kanji translation...")
    translator = KanjiTranslator()
    
    # Test single Kanji
    result = translator.translate_kanji('日')
    assert result is not None, "Failed to translate '日'"
    assert 'meanings' in result, "Result missing 'meanings' field"
    assert 'sun' in result['meanings'] or 'day' in result['meanings'], "Incorrect translation for '日'"
    print("✓ Single Kanji translation works")
    
    # Test text with multiple Kanji
    results = translator.translate_text('日本')
    assert len(results) == 2, "Failed to translate '日本'"
    assert results[0]['kanji'] == '日', "First character should be '日'"
    assert results[1]['kanji'] == '本', "Second character should be '本'"
    print("✓ Multiple Kanji translation works")
    
    # Test unknown Kanji
    result = translator.translate_kanji('鬱')  # Complex kanji not in dictionary
    assert result is None, "Should return None for unknown Kanji"
    print("✓ Unknown Kanji handling works")
    
    print("\nAll tests passed! ✓")


def test_format_translation():
    """Test translation formatting"""
    print("\nTesting translation formatting...")
    translator = KanjiTranslator()
    
    result = translator.translate_kanji('日')
    formatted = translator.format_translation({
        'kanji': '日',
        'translation': result
    })
    
    assert '日' in formatted, "Formatted output should contain the Kanji"
    assert 'sun' in formatted or 'day' in formatted, "Formatted output should contain meanings"
    print("✓ Translation formatting works")
    print("\nFormatted output sample:")
    print(formatted)


def test_common_words():
    """Test translation of common Japanese words"""
    print("\n\nTesting common Japanese words...")
    translator = KanjiTranslator()
    
    test_words = [
        ('日本', 2, 'Japan'),
        ('日本語', 3, 'Japanese language'),
        ('学校', 2, 'school'),
        ('先生', 2, 'teacher'),
        ('学生', 2, 'student'),
    ]
    
    for word, expected_count, description in test_words:
        results = translator.translate_text(word)
        assert len(results) == expected_count, f"Failed to translate all Kanji in '{word}' ({description})"
        print(f"✓ '{word}' ({description}) - {expected_count} Kanji translated")
    
    print("\nAll common word tests passed! ✓")


def main():
    """Run all tests"""
    print("=" * 60)
    print("Kanji Translator Test Suite")
    print("=" * 60)
    
    test_basic_translation()
    test_format_translation()
    test_common_words()
    
    print("\n" + "=" * 60)
    print("All tests completed successfully! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
