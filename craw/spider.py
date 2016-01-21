#!/usr/bin/env python
# coding:utf8
# By:dub

import urllib2


class WebSpider:
    def __init__(self, url, useragent=None):
        self.url = url
        self.useragent = useragent

    def get_response(self):
        response = urllib2.urlopen(self.url)
        if response.code == 200:
            return response.read()
        else:
            return None
