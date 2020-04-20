"""rename record.id in fasta file with filename"""
import os
from Bio import SeqIO
from optparse import OptionParser

def rename(path, outpath):
    for files in os.listdir(path):
        filename = files.split('_protein')[0]
        handle = open(path + files)
        outfile = open(outpath + '{}'.format(filename), "w")
        for record in SeqIO.parse(handle, "fasta"):
            record.id = '{}'.format(filename)+'|'
            SeqIO.write(record, outfile, "fasta")
        outfile.close()
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=rename\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-p : directory to the fasta files
\n\t\t\t\t\t-o : directory to output files""") 
parser.add_option("-p", "--path", help="directory to the fasta files")
parser.add_option("-o", "--outpath", help="directory to output files")    
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "rename":
    print('ok')
    rename(opt.path, opt.outpath)
