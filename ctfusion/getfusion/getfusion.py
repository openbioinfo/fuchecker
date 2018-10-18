#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

def getfusion ():
    '''
    find fusion reads from split or discordant sam file
    '''
    dic = {}
    #open fusion_file get target gene data

    with open(fusion_file) as fusion_data:
        for line in fusion_data:
            (chro,start,end,gene) = line.split()
            for i in range(start-end+1):
                num = start+i
                key = chro+':'+num
                dic[key] = gene

    #find fusion in target region


    #check fusion is right

if __name__ == "__main__":
    import sys
    fusion_file = sys.argv[1]
    prefix = sys.argv[2]
    getfusion(fusion_file,prefix)
