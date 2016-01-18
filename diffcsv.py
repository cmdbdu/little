#!/usr/bin/env python
# coding:utf8
# By:dub
import csv

def openfile():

    devicefile = open('exist1.csv')
    allline = csv.DictReader(devicefile)

    newfile = open('newcsv.csv','w')
    fields = allline.fieldnames
    fields.append('field')
    writer = csv.DictWriter(newfile, fields)

    for line in allline:
        csvfile = open('exist2.csv')
        comment = csv.DictReader(csvfile)
        for row in comment:
            # 两个对比的字段，license和key_id
            if line['license'] == row['key_id']:
                line['field']='Y'
        writer.writerow(line)

if __name__ == '__main__':
    openfile()
