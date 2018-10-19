# /usr/bin/env python
# -*- coding:utf8 -*-

import os

def test_ctgusion(test_soft,sam,fusion_file,prefix,output):
    
    cmd = "python %s -i %s -f %s -p %s -o %s" % (test_soft,sam,fusion_file,prefix,output)
    print cmd
    os.system(cmd)


if __name__ == "__main__":
    sam = "/4_disk/workspace/tuxn/git/ctfusion/tests/data/ZG-RNAPC.sam"
    output = "/4_disk/workspace/tuxn/git/ctfusion/tests/"
    fusion_file = "/4_disk/workspace/tuxn/git/ctfusion/tests/data/fusion.bed"
    prefix = "001"
    test_soft = "/4_disk/workspace/tuxn/git/ctfusion/bin/ctfusion.py"
    test_ctgusion(test_soft,sam,fusion_file,prefix,output)
