#!/usr/bin/env python

import re
import urllib.parse
import urllib.request


def shorten(long_url):
    """
    Shorten a long url into a shorter one
    :param long_url: Your long url
    :return: A short ur1.ca one
    """
    data = urllib.parse.urlencode({
        'submit': 'Make it an ur1!',
        'longurl': long_url,
    }).encode()
    req = urllib.request.urlopen('http://ur1.ca/', data=data)
    out = req.read().decode()
    req.close()
    match = re.search(
        '<p class="success">Your ur1 is: <a href="http://ur1.ca/(?P<string>.*?)">http://ur1.ca/(?P=string)</a></p>',
        out
    )

    return 'http://ur1.ca/' + match.group('string')
