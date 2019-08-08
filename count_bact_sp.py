"""
Count strains of bacterial species from the GenBank and RefSeq.
As an input use files obtained from the get_bact_list.py
"""

import urllib.request as urllib2
import csv
from optparse import OptionParser
import sys



def count_bact_v1(genbank_file):
    orig_stdout = sys.stdout
    output = open("bact_count_genbank.csv", "wt")
    sys.stdout = output
    splist = [s.strip('\n') for s in open(genbank_file, 'r')]
    for i in splist:
        sp_name = i.strip('\n')
        req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/{}/assembly_summary.txt'.format(sp_name))
        response = urllib2.urlopen(req)
        the_page = response.read()
        print(i, '\t', len(str(the_page).split('\\n')) - 3)
    sys.stdout = orig_stdout
    output.writeheader()
    output.writerow()

def count_bact_v2(refseq_file):
    orig_stdout = sys.stdout
    output = open("bact_count_refseq.csv", "wt")
    sys.stdout = output
    spname = [s.strip('\n') for s in open(refseq_file, 'r')]
    for i in spname:
        sp_name = i.strip('\n')
        req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/{}/assembly_summary.txt'.format(sp_name))
        response = urllib2.urlopen(req)
        the_page = response.read()
        print(i, '\t', len(str(the_page).split('\\n')) - 3)
    sys.stdout = orig_stdout
    output.writeheader()
    output.writerow()

parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=genbank.\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-g : list of bacterial species from genbank
\t\t\t\t\t=refseq.\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-r : list of bacterial species from refseq""") 

parser.add_option("-g", "--genbank_file", help="List of bacteria obtained from GenBank. output='bact_count_genbank.csv")
parser.add_option("-r", "--refseq_file", help="List of bacteria obtained from RefSeq. output='bact_count_refseq.csv")
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "genbank":
    print('Let\'s start counting from the GenBank')
    count_bact_v1(opt.genbank_file)
elif opt.task == "refseq":
    print('Let\'s start counting from the RefSeq')
    count_bact_v2(opt.refseq_file)


