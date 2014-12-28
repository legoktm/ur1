#!/usr/bin/env python

import unittest
import ur1


class Ur1Test(unittest.TestCase):
    def test_known_urls(self):
        data = {
            'http://www.google.com': 'http://ur1.ca/1n',
            'https://en.wikipedia.org': 'http://ur1.ca/j8yel',
            'https://python.org': 'http://ur1.ca/j8yek',
        }
        for long_url, short_url in data.items():
            self.assertEqual(short_url, ur1.shorten(long_url))


if __name__ == '__main__':
    unittest.main()
