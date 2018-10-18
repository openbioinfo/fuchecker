#!/usr/bin/env python
# coding:utf-8
import sys
import os
dirpath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"../")
sys.path.insert(0,dirpath)
from ctfusion.samblaster.samblaster import samblaster
from ctfusion.getfusion.getfusion import getfusion

def main(sam,fusion_file,prefix):
    
    #samblaster
    samblaster(sam,prefix)
    #getfusion
    getfusion(fusion_file,prefix)

    return finish

if __name__ == "__main__":
    from docopt import docopt
    Usage = """
    Usage:
        ctfusion.py -i <sam> -f <fusions> -p <prefix>

    Options:
        -i,--input=<bam>          input sam files
        -f,--fusion=<fusions>     fusions list file
        -p,--prefix=<prefix>      output prefix  

    """
    args = docopt(Usage)
    sam = args["--input"]
    fusion_file = args["--fusion"]
    prefix = args["--prefix"]
    main(sam,fusion_file,prefix)
