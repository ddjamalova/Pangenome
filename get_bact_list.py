"""
Get list of bacterial species from the GenBank and RefSeq
"""

import urllib.request as urllib2
import sys
from os import system
from optparse import OptionParser

def get_bac_genbank():
    orig_stdout = sys.stdout
    output = open('bact_list_genbank', 'w')
    sys.stdout = output
    req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/')
    response = urllib2.urlopen(req)
    the_page = response.read()
    for i in str(the_page).split('\\r\\n'):
        print(i.split()[-1])
    sys.stdout = orig_stdout
    output.close()

def get_bac_refseq():
    orig_stdout = sys.stdout
    output = open('bact_list_refseq', 'w')
    sys.stdout = output
    req = urllib2.Request('ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/')
    response = urllib2.urlopen(req)
    the_page = response.read()
    for i in str(the_page).split('\\r\\n'):
        print(i.split()[-1])
    sys.stdout = orig_stdout
    output.close()

parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=genbank.\n\r
\n\t\t\t\t\treturn list of bacteria from GenBank as bact_list_genbank file
\t\t\t\t\t=refseq.\n
\t\t\t\t\t\treturn list of bacteria from RefSeq as bact_list_refseq file""") 
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "genbank":
    print('Hello GenBank!')
    get_bac_genbank()
elif opt.task == "refseq":
    print('Hello RefSeq!')
    get_bac_refseq()
