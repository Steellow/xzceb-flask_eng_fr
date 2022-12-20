
import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french(None), "asd")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english(None), "asd")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()
