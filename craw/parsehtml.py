#!/usr/bin/env python
# coding:utf8
# By:dub

import time
import re
from bs4 import BeautifulSoup
from urlmange import Mange


class ParseHtml:
    def __init__(self, data, new_urls, old_urls):
        self.data = data
        self.new_urls = new_urls
        self.old_urls = old_urls

    def get_label_a(self):
        try:
            soup = BeautifulSoup(self.data, 'lxml')
            alist = soup.find_all('a')
            mange = Mange(self.new_urls, self.old_urls)
            for i in alist:
                if 'http://' in i['href']:
                    mange.add_new_urls(i['href'])
        except Exception,e:  # no href
            pass
