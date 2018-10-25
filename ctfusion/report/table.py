#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

def table (result_path,prefix,report_path):
    '''
    out put fusion report as table
    '''
    get,fu_data,gene,sumfu = {},[],[],{}
    result_file = result_path+prefix+".find_fusion.txt"
    with open(result_file) as result:
        for line in result:
            fu_data = line.split()
            gene = fu_data[0].split(':')
            key = gene[1]+':'+gene[0]
            get[fu_data[0]] = fu_data[1]
            if key in get:
                sumfu[key] = int(get[key])+int(fu_data[1])
    
    report_file = report_path+prefix+".report.xls"
    with open(report_file,"w") as out:
        for result in sumfu.keys():
            pri = result+"\t"+str(sumfu[result])+"\n"
            out.write(pri)

    print "report out"


if __name__ == "__main__":
    import sys
    result_path = sys.argv[1]
    prefix = sys.argv[2]
    report_path = sys.argv[3]
    getfusion(result_path,prefix,report_path)
