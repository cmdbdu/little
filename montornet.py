#coding:utf8
import sys
import time

filename = '/proc/net/dev'

def start():
    now = time.time()
    content = open(filename)
    for line in content.readlines():
        if line.find("eth0") > 0:
            field = line.split()
            recv = field[0].split(":")[1]
            recv = recv or field[1]
            send = field[8]
    print 'recv:%s,send:%s,time:%s' % (recv,send, now)
    content.close()

if __name__ == "__main__":
    i = 0
    while i < 100:
        time.sleep(2)
        start()
        i += 1
