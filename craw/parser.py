#!/usr/bin/env python
# coding:utf8
# By:dub

import argparse

parser = argparse.ArgumentParser(description="process some intergers")
parser.add_argument("-u","--url",
                    help="eg:http://www.xxx.com")
parser.add_argument("-p","--page",
                    default=20,
                    choices=[50, 100, 200],
                    type=int,
                    help="max page number")
parser.add_argument("-t","--thread",
                    default=5,
                    choices=[10, 20, 50],
                    type=int,
                    help="max thread number")


args = parser.parse_args()

