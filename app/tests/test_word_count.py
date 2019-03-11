import unittest
from controllers.controller import WordCounter


class TestWordCountString(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordCounter()

    def tearDown(self):
        self.word_counter = None

    def test_count_from_short_string(self):
        expected = 5
        test = "fit is good fit fitting, and fits is afit a fit, and fit is good, fit"
        result = self.word_counter.count_from_string(test, "fit")
        self.assertEqual(expected, result,
                         "Error, the counting number is not correct !")

    def test_count_from_long_string(self):
        expected = 20
        test = "fit is good fit fitting, and fits is afit a fit, and fit is good, fit fit is good fit fitting, and fits is afit a fit, and fit is good, fit fit is good fit fitting, and fits is afit a fit, and fit is good, fit fit is good fit fitting, and fits is afit a fit, and fit is good, fit"
        result = self.word_counter.count_from_string(test, "fit")
        self.assertEqual(expected, result,
                         "Error, the counting number is not correct !")
