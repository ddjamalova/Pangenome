"""
Count strains of bacterial species from the GenBank and RefSeq.
As an input use files obtained from the get_bact_list.py
Redirect output using > output
"""
import urllib.request as urllib2
import sys
import os
from optparse import OptionParser

def count_bac_genbank(genbank_list):
    splist = [s.strip('\n') for s in open(genbank_list, 'r')]
    for i in splist:
        try:
            sp_name = i.strip('\n')
            req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/{}/assembly_summary.txt'.format(sp_name))
            response = urllib2.urlopen(req)
            the_page = response.read()
            print(i, '\t', len(str(the_page).split('\\n')) - 3) 
        except Exception:
            continue
def count_bac_refseq(refseq_list):
    splist = [s.strip('\n') for s in open(refseq_list, 'r')]
    for i in splist:
        try:
            sp_name = i.strip('\n')
            req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/{}/assembly_summary.txt'.format(sp_name))
            response = urllib2.urlopen(req)
            the_page = response.read()
            print(i, '\t', len(str(the_page).split('\\n')) - 3) 
        except Exception:
            continue
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=genbank\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-g : list of bacterial species from genbank
\t\t\t\t\t=refseq\n
\n\t\t\t\t\tRequired option
\n\t\t\t\t\t-r : list of bacterial species from refseq""")
parser.add_option("-g", "--genbank_list", help = "List of bacterial species")
parser.add_option("-r", "--refseq_list", help = "List of bacterial species")
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "genbank":
    count_bac_genbank(opt.genbank_list)
elif opt.task == "refseq":
    count_bac_refseq(opt.refseq_list)


