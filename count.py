#coding:utf8

self_sound = ['a', 'e', 'i', 'o', 'u']
s = raw_input()

for i in self_sound:
    if s.count(i):
        print i+ ':%d ' % s.count(i)
