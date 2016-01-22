#!/usr/bin/env python
# coding:utf8
# By:dub

def refacstrip():
    string = raw_input('input a string:')
    output_str = raw_input('input a str too:')
    print main(string, output_str)

def main(str1,delstr):
    if str1.startswith(delstr):
        str1 = str1.split(delstr)[-1]
        main(str1,delstr)
    elif str1.endswith(delstr):
        str1 = str1.split(delstr)[0]
        main(str1,delstr)
    return str1



if __name__ == "__main__":
    refacstrip()
