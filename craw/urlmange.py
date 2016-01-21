#!/usr/bin/env python
# coding:utf8
# By:dub

class Mange:
    def __init__(self, new_urls, old_urls):
        self.new_urls = new_urls
        self.old_urls = old_urls

    def add_new_urls(self, url):
        if url not in self.old_urls:
            self.new_urls.add(url)

    def add_old_urls(self, url):
        if url not in self.old_urls:
            self.old_urls.add(url)

    def has_new_urls(self):
        return len(self.new_urls) != 0

    def pop(self):
        return self.new_urls.pop()
