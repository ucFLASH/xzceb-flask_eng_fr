"""
Module for English to French and French to English translation using MyMemoryTranslator.
"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """
    Translates English text to French using the MyMemoryTranslator module.

    Args:
        englishtext (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    frenchtext = MyMemoryTranslator(source='en', target='fr').translate(englishtext)
    print (frenchtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """
    Translates French text to English using the MyMemoryTranslator module.

    Args:
        frenchtext (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    englishtext = MyMemoryTranslator(source='fr', target='en').translate(frenchtext)
    print (englishtext)
    return englishtext

# Added final newline
print()
