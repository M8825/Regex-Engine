import unittest
from regex import RegexEngine


class TestRegex(unittest.TestCase):
    def test_equal_length(self):
        self.assertEqual(RegexEngine('aaa', 'aaa').equal_length(), True,
                         'Valid equal length regEx was declined')
        self.assertEqual(RegexEngine('.a.', 'aaa').equal_length(), True,
                         'Valid equal length regEx was declined')
        self.assertEqual(RegexEngine('..b', 'aaa').equal_length(), False,
                         'Invalid equal length regEx was accepted')

    def test_unequal_sting(self):
        self.assertTrue(RegexEngine('app', 'apple').unequal_string(),
                        'Valid stage 3 regEx was declined')
        self.assertTrue(RegexEngine('app', 'apple peach').unequal_string(),
                        'Valid stage 3 regEx was declined')
        self.assertFalse(RegexEngine('234', 'apple').unequal_string(),
                         'Invalid stage 3 regEx was accepted')

    def test_metacharacters(self):
        self.assertTrue(RegexEngine('^app', 'apple').metacharacters())
        self.assertTrue(RegexEngine('le$', 'apple').metacharacters())
        self.assertTrue(RegexEngine('^a', 'apple').metacharacters())
        self.assertTrue(RegexEngine('.$', 'apple').metacharacters())
        self.assertTrue(RegexEngine('apple$', 'tasty apple').metacharacters())
        self.assertTrue(RegexEngine('^apple', 'apple pie').metacharacters())
        self.assertTrue(RegexEngine('^apple$', 'apple').metacharacters())

        self.assertFalse(RegexEngine('^apple$', 'tasty apple').metacharacters())
        self.assertFalse(RegexEngine('^apple$', 'apple pie').metacharacters())
        self.assertFalse(RegexEngine('app$', 'apple').metacharacters())
        self.assertFalse(RegexEngine('^le', 'apple').metacharacters())


if __name__ == "__main__":
    unittest.main()