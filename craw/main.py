#!/usr/bin/env python
# coding:utf8
# By:dub

import time
import threading
from parser import args
from urlmange import Mange
from spider import WebSpider
from parsehtml import ParseHtml


class SpiderThread(threading.Thread):

    def __init__(self, url, pages, deep, new_urls, old_urls):
        threading.Thread.__init__(self)
        self.maxdeep = deep
        self.maxpages = pages
        self.url = url
        self.new_urls = new_urls
        self.old_urls = old_urls

    def start(self):
        try:
            sp = WebSpider(self.url)
            response = sp.get_response()
            p = ParseHtml(response, new_urls, old_urls)
            p.get_label_a()
        except Exception,e:
            print e


def main():

    # page thread url
    if not args.url:
        return

    mange = Mange(new_urls, old_urls)
    mange.add_new_urls(args.url)
    while mange.has_new_urls():
        if len(old_urls) >= args.page:
            break
        try:
            url = mange.pop()
            myt = SpiderThread(url, args.page, args.thread, new_urls, old_urls)
            myt.start()
            mange.add_old_urls(url)
        except Exception,e:
            print e
        time.sleep(1)



if __name__ == "__main__":
    new_urls = set()
    old_urls = set()
    main()
