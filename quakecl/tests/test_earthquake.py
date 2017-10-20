import unittest
from datetime import date

from quakecl import earthquake


class Tests(unittest.TestCase):

    def test_convert_to_date(self):
        got = earthquake.convert_to_date('1995-07-10')
        expected = date(1995, 7, 10)
        self.assertEqual(got, expected)

    def test_get_page(self):
        result = earthquake.get_page('http://abcde.fghij')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
