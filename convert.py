'''
Convert faa to fasta
'''
import os
from optparse import OptionParser

faa = '.faa'
fasta = '.fasta'
def getfasta(path, faa, fasta):
    for files in os.listdir(path):
        if files.endswith(faa):
            src = files.split(faa)[0]
            source = files.strip()
            os.rename(path + source, path + src + fasta)
    
def getfaa(path, faa, fasta):
    for files in os.listdir(path):
        if files.endswith(fasta):
            src = files.split(faa)[0]
            source = files.strip()
            os.rename(path + source, path + src + faa)
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=fasta to get .fasta files.
\t\t\t\t\t=faa to get .faa files.\n
\n\t\t\t\t\tRequires options:
\n\t\t\t\t\t-p : Directory with files""")
parser.add_option("-p", "--path", help="Directory with fasta files")
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "fasta":
    getfasta(opt.path, faa, fasta)

if opt.task == "faa":
    getfaa(opt.path, faa, fasta)
print("Done")
