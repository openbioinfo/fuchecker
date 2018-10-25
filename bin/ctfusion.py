#!/usr/bin/env python
# coding:utf-8
import sys
import os
dirpath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"../")
sys.path.insert(0,dirpath)
from ctfusion.samblaster.samblaster import samblaster
from ctfusion.getfusion.getfusion import getfusion
from ctfusion.report.table import table

def ctfusion(sam,fusion_file,prefix,output):
    
    #samblaster
    samblaster(sam,prefix,output)
    #getfusion
    getfusion(fusion_file,prefix,output)
    #report
    table(output,prefix,output)
    return "finish!"

if __name__ == "__main__":
    from docopt import docopt
    Usage = """
    Usage:
        ctfusion.py -i <sam> -o <output_path> -f <fusions> -p <prefix>

    Options:
        -i,--input=<sam>          input sam files
        -f,--fusion=<fusions>     fusions list file
        -p,--prefix=<prefix>      output prefix
        -o,--output=<path>        output path

    """
    args = docopt(Usage)
    sam = args["--input"]
    fusion_file = args["--fusion"]
    prefix = args["--prefix"]
    output = args["--output"]
    check_path = output[-1:]
    if check_path != '/':
        output = output+'/'
    ctfusion(sam,fusion_file,prefix,output)
