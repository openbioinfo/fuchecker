#!/usr/bin/env python
# coding:utf-8

import yaml
try:
    from config import bwa_soft
except:
    bwa_soft = "bwa"
import os,sys
from jbiot import yamladd

def bwa(yml):
    """bwa mem fastqs to bam file

    Args:
        params : key is `yaml`,value is yaml file::

            fastqs      :fastq files
            reference   :reference file for bwa
            bwa_args    :extra args for map

    Returns:
        dict : key is `yaml`,value is yaml file

    """ 
    # handle input
    indict = yaml.load(open(yml).read())
    fastqs = indict["format_fastqs"]
    ref = indict["reference"]
    sampleid = indict["sampleid"]

    # process cmd
    for fqs in fastqs.items():
        fq1 = fqs[0]
        fq2 = fqs[1]
        sam = sampleid+'.sam'
        r_args = "@RG\\tID:%s\\tSM:%s\\tLB:%s\\tPL:ILLUMINA" % (sampleid,sampleid,sampleid)
        cmd = "%s mem -t 4 -M -R '%s' %s %s %s > %s" % (bwa_soft,r_args,ref,fq1,fq2,sam)
        log.run("bwa mapping",cmd)

    # handle output
    outdict = {}
    outdict["sam"] = sam
    out = yamladd(yml,outdict)
    return out
