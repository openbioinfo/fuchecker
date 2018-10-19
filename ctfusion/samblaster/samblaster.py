#!/usr/bin/env python
# coding:utf-8

import sys
import os

try:
    from config import samblaster_soft
except:
    samblaster_soft = "samblaster"

def samblaster (sam,prefix,outpath):
    
    disc_sam = outpath+prefix+".disc.sam"
    split_sam = outpath+prefix+".split.sam"
    out_sam = outpath+prefix+".out.sam"
    cmd = "%s -i %s -e -d %s -s %s -o %s" % (samblaster_soft,sam,disc_sam,split_sam,out_sam)
    print cmd
    os.system(cmd)


if __name__ == "__main__":
    import sys
    sam = sys.argv[1]
    prefix = sys.argv[2]
    outpath = sys.argv[3]
    samblaster(sam,prefix,outpath)
