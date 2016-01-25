#!/usr/bin/env python
# coding:utf8
# By:dub
import os
import pprint


def get_file_list(code_dir):
    codefile_list  = os.listdir(code_dir)
    for i in range(len(codefile_list)):
        codefile_list[i] = os.path.join(code_dir,codefile_list[i])
    return codefile_list


def countcodelines(filename):
    content = {}

    f = open(filename,'r')
    l = f.readlines()

    content['len'] = len(l)
    notes = 0
    for i in l:
        if i.startswith('#'):
            notes = notes+1
    content['notes'] = notes
    content['codes'] = len(l)-notes

    return content


def main(listfile):
    for i in listfile:
        if os.path.isdir(i):
            filelist = get_file_list(i)
            main(filelist)
        elif i.endswith('py'):
            countcodelines(i)
            record[i] = countcodelines(i)

if __name__ == "__main__":

    record = {}
    base_dir = './'
    ll = get_file_list(base_dir)
    main(ll)

    pprint.pprint(record)

