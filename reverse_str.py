#coding:utf8
import sys

def fun():
    s = raw_input('please input something:')
    
    #1
    s1 = s[::-1]
    print 'first method result:',  s1

    #2
    s2 = list(s)
    s2.reverse()
    print 'second method result:', ''.join(s2)



if __name__ == "__main__":
    fun()
