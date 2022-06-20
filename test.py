import unittest
from main import *


class TestMain(unittest.TestCase):

    # def test_encrypt_none(self):
    #     encode(None)
    #     self.assertIsNone()

    def test_encode_decode_returns_expected_string_as_upper(self):
        expected_value = "Hello world"

        encoded = encode(expected_value)
        actual_value = decode(encoded)

        self.assertEqual(actual_value, expected_value.upper())

    def test_encode_decode_returns_expected_string_maintaining_whitespace_at_end(self):
        expected_value = "Hello world      "

        encoded = encode(expected_value)
        actual_value = decode(encoded)

        self.assertEqual(actual_value, expected_value.upper())

    def test_decode_with_invalid_morse_returns_empty_string(self):
        self.assertEqual(decode("Hello world"), "")

    def test_encode_decode_with_extra_whitespace_returns_expected_value(self):
        expected_value = "Hello world"

        encoded = "   " + encode(expected_value) + "   "
        actual_value = decode(encoded)

        self.assertEqual(actual_value, expected_value.upper())

    def test_encode_decode_with_unexpected_special_character_returns_decoded_without_special_character(self):
        expected_value = "Hello world"

        encoded = encode(expected_value + '!')
        actual_value = decode(encoded)

        self.assertEqual(actual_value, expected_value.upper())

