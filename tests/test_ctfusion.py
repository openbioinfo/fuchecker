# /usr/bin/env python
# -*- coding:utf8 -*-

import os

def test_ctfusion(test_soft,sam,fusion_file,prefix,output):
    
    cmd = "python %s -i %s -f %s -p %s -o %s" % (test_soft,sam,fusion_file,prefix,output)
    print cmd
    os.system(cmd)


if __name__ == "__main__":
    sam = "./data/ZG-RNAPC.sam"
    output = "./"
    fusion_file = "./data/fusion.bed"
    prefix = "001"
    test_soft = "../bin/ctfusion.py"
    test_ctfusion(test_soft,sam,fusion_file,prefix,output)
