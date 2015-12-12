#coding:utf8
#dof mean dir or file

import os

def get_cwd():
    
    dirc = os.getcwd()
    return dirc

def get_list(DIR):
    
    list_dir = os.listdir(DIR)
    
    return list_dir

def is_dir(cwd, dirlist):
    for i in dirlist:
        filename = cwd + '/%s' % i
        if os.path.isdir(filename):
            print filename+': dir'
        else:
            print filename+': file'

if __name__ == '__main__':
    
    is_dir(get_cwd(),get_list(get_cwd()))
