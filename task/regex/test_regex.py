import unittest
from regex import check_string, check_word


class TestRegex(unittest.TestCase):
    def test_check_word(self):
        self.assertTrue(check_word('colou?r', 'color'), 'colou?r|color')
        self.assertTrue(check_word('colou?r', 'colour'), 'colou?r|colour')
        self.assertTrue(check_word('colou*r', 'color'), 'colou*r|color')
        self.assertTrue(check_word('colou*r', 'colour'), 'colou*r|colour')
        self.assertTrue(check_word('colou*r', 'colouur'), 'colou*r|colour')
        self.assertTrue(check_word('col.*r', 'color'), 'colou*r|colouur')
        self.assertTrue(check_word('col.*r', 'colour'), 'col.*r|colour')
        self.assertTrue(check_word('col.*r', 'colr'), 'col.*r|colr')
        self.assertTrue(check_word('col.*r', 'collar'), 'col.*r|collar')
        self.assertFalse(check_word('col.*r$', 'colors'), 'col.*r$|colors')
        self.assertFalse(check_word('colou?r', 'colouur'), 'colou?r|colouur')

    def test_check_string(self):
        self.assertTrue(check_string('a', 'a'), 'a|a')
        self.assertTrue(check_string('^app', 'apple'), '^app|apple')
        self.assertTrue(check_string('le$', 'apple'), 'le$|apple')
        self.assertTrue(check_string('^a', 'apple'), '^a|apple')
        self.assertTrue(check_string('.$', 'apple'), '.$|apple')
        self.assertTrue(check_string('apple$', 'tasty apple'), 'apple$|tasty apple')
        self.assertTrue(check_string('^apple', 'apple pie'), '^apple|apple pie')
        self.assertTrue(check_string('^apple$', 'apple'), '^apple$|apple')
        self.assertFalse(check_string('^apple$', 'tasty apple'), '^apple$|tasty apple')
        self.assertFalse(check_string('^apple$', 'apple pie'), '^apple$|apple pie')
        self.assertFalse(check_string('app$', 'apple'), 'app$|apple')
        self.assertFalse(check_string('^le', 'apple'), '^le|apple')


if __name__ == "__main__":
    unittest.main()