#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

def getfusion (fusion_file,prefix,outpath):
    '''
    find fusion reads from split or discordant sam file
    '''
    dic,disc_data,split_data,get = {},[],[],{}
    #open fusion_file get target gene data
    print "start get fusion"
    with open(fusion_file) as fusion_data:
        for line in fusion_data:
            (chro,start,end,gene) = line.split()
            start,end = int(start),int(end)
            for i in range(abs(end-start)+1):
                num = start+i
                key = chro+':'+str(num)
                dic[key] = gene

    #find fusion in target region
    
    disc_sam = outpath+prefix+".disc.sam"
    split_sam = outpath+prefix+".split.sam"
    with open(disc_sam) as disc:
        for line in disc:
            disc_data = line.split()
            if disc_data[0][0] == '@':
                continue
            point1 = disc_data[2]+':'+disc_data[3]
            if disc_data[6] == '=':
                disc_data[6] = disc_data[2]
            point2 = disc_data[6]+':'+disc_data[7]
            if point1 in dic and point2 in dic:
                if dic[point1] == dic[point2]:
                    continue
                getfusion = dic[point1]+":"+dic[point2]
                if getfusion in get:
                    get[getfusion] += 1
                else:
                    get[getfusion] = 1
    
    with open(split_sam) as disc:
        for line in disc:
            disc_data = line.split()
            if disc_data[0][0] == '@':
                continue
            point1 = disc_data[2]+':'+disc_data[3]
            if disc_data[6] == '=':
                disc_data[6] = disc_data[2]
            point2 = disc_data[6]+':'+disc_data[7]
            if point1 in dic and point2 in dic:
                if dic[point1] == dic[point2]:
                    continue
                getfusion = dic[point1]+":"+dic[point2]

    #check fusion is right

    #out print fusion

    for key in get.keys():
        print key,get[key]

if __name__ == "__main__":
    import sys
    fusion_file = sys.argv[1]
    prefix = sys.argv[2]
    outpath = sys.argv[3]
    getfusion(fusion_file,prefix,outpath)
