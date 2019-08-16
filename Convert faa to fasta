'''
Convert faa to fasta
'''
import os
from optparse import OptionParser

faa = '.faa'
fasta = '.fasta'
def change_format(path, faa, fasta):
    for files in os.listdir(path):
        if files.endswith(faa):
            src = files.split(faa)[0]
            source = files.strip()
            os.chdir(outpath)
            os.rename(path + source, path + src + fasta)
parser = OptionParser()
parser.add_option("-p", "--path", help="Directory with .faa files")
opt, args = parser.parse_args()
change_format(opt.path, faa, fasta)
print("Done")
