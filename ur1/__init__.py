#!/usr/bin/env python

import re
import sys

if sys.version[0] == '3':
    from urllib.parse import urlencode
    from urllib.request import urlopen
else:
    from urllib import urlencode, urlopen


def shorten(long_url):
    """
    Shorten a long url into a shorter one
    :param long_url: Your long url
    :return: A short ur1.ca one
    """
    data = urlencode({
        'submit': 'Make it an ur1!',
        'longurl': long_url,
    }).encode()
    req = urlopen('http://ur1.ca/', data=data)
    out = req.read().decode()
    req.close()
    match = re.search(
        '<p class="success">Your ur1 is: <a href="http://ur1.ca/(?P<string>.*?)">http://ur1.ca/(?P=string)</a></p>',
        out
    )

    return 'http://ur1.ca/' + match.group('string')
