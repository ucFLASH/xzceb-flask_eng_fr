import unittest
from unittest.mock import patch
from translator import englishtofrench, frenchtoenglish

class TranslatorTest(unittest.TestCase):

    def test_englishtofrench(self):
        with patch('translator.MyMemoryTranslator') as mock_translator:
            mock_translator.return_value.translate.return_value = "Bonjour"
            result = englishtofrench("Hello")
            mock_translator.assert_called_once_with(source='en', target='fr')
            mock_translator.return_value.translate.assert_called_once_with("Hello")
            self.assertEqual(result, "Bonjour")

    def test_frenchtoenglish(self):
        with patch('translator.MyMemoryTranslator') as mock_translator:
            mock_translator.return_value.translate.return_value = "Hello"
            result = frenchtoenglish("Bonjour")
            mock_translator.assert_called_once_with(source='fr', target='en')
            mock_translator.return_value.translate.assert_called_once_with("Bonjour")
            self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
