

def main():
    pass

if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
        ctfusion.py -i <bam> -f <fusions> -p <prefix>

    Options:
        -i,--input=<bam>          input bam files
        -f,--fusion=<fusions>     fusions list file
        -p,--prefix=<prefix>      output prefix  

    """
