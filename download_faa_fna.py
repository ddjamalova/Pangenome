"""
Get data for Pangenome analysis

1. Download assembly_summary.txt files of defined bacteria
   input: list of bacteria obtained from the get_bact_list.py
2. Prepare assembly_summary.txt -> get url for ftp <- sampling
   output: assembly_summary.txt with url
3. Downlaod files with "_protein.faa" and "_cds_from_genomic.fna" identifiers
   version = "latest_assembly_version" or "all_assembly_versions"
"""

import sys
import os
from os import system
import random
from optparse import OptionParser

faa_id = "_protein.faa.gz"
fna_id = "_cds_from_genomic.fna.gz"
ncbi_dir = "ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/"
sample_size_1 = 1
sample_size_5 = 5
def get_assemb_sum_genbank(filename, path):
    splist = open(filename, 'r')
    for s in splist:
        sp_name = s.strip('\n')
        for s in sp_name:
            try:
                os.chdir(path)
                system('curl ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/{}/assembly_summary.txt'.format(sp_name) + '>' + sp_name)
                break
            except:
                continue
            
def prepare_files_5(path, sample_size_5):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\n') for s in open(path + files, 'r')]
        if (len(filelist) - 2) >= 5:
            data = random.sample(filelist[2:], 5)
            outfiles = os.path.join(path, filename + ".txt")
            outfile = open(outfiles, 'w')
            for lines in data:
                line = lines.split('\t')
                outfile.write(line[-3] + '\n')
            outfile.close()
    for files in os.listdir(path):
        if not files.endswith(".txt"):
            os.remove(path + files)


def prepare_files_1(path, sample_size_1):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\n') for s in open(path + files, 'r')]
        if (len(filelist) - 2) == 1:
            data = random.sample(filelist[2:], 1)
            outfiles = os.path.join(path, filename + ".txt")
            outfile = open(outfiles, 'w')
            for lines in data:
                line = lines.split('\t')
                outfile.write(line[-3] + '\n')
            outfile.close()

# Download protein fasta files
def download_faa(path, faa_id, version, ncbi_dir, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        with open(path + files) as f:
            for line in f:
                url_dir = []
                url_dir.append(line.split('\n')[0])
                for line in url_dir:
                    data = line.split('/')[9]
                    os.chdir(outpath)
                    os.system("wget\t" + ncbi_dir + filename + "/" + version + "/" + data + "/" + data + faa_id)
               
                    
# Download nucleotide fasta files
def download_fna(path, fna_id, version, ncbi_dir, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        with open(path + files) as f:
            for line in f:
                url_dir = []
                url_dir.append(line.split('\n')[0])
                for line in url_dir:
                    data = line.split('/')[9]
                    os.chdir(outpath)
                    os.system("wget\t" + ncbi_dir + filename + "/" + version + "/" + data + "/" + data + fna_id)
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=assembly_summary\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-f : list of bacterial species
\n\t\t\t\t\t-d : directory to save assembly summary files
\t\t\t\t\t=sampling_5\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\t\t\t\t\t=sampling_1\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\t\t\t\t\t=get_faa\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-v : choose all_assembly_versions or latest_assembly_versions
\n\t\t\t\t\t-o : directory for output files
\t\t\t\t\t=get_fna\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-v : choose "all_assembly_versions" or "all_assembly_versions
\n\t\t\t\t\t-o : directory for output files""") 
parser.add_option("-f", "--filename", help="List of bacteria obtained from the GenBank")
parser.add_option("-d", "--path", help="Directory with assembly summary files")
parser.add_option("-v", "--version", help="latest_assembly_versions or all_assembly_versions")
parser.add_option("-o", "--outpath", help="Directory for output files")

opt, args = parser.parse_args()
print(opt.task)
if opt.task == "assembly_summary":
    print('Downloading assembly summary files')
    get_assemb_sum_genbank(opt.filename, opt.path)
elif opt.task == "sampling_5":
    print('Sampling species with 5 or more strains')
    prepare_files_5(opt.path, sample_size_5)
elif opt.task == "sampling_1":
    print('Sampling species with 1 strain')
    prepare_files_1(opt.path, sample_size_1)
elif opt.task == "get_fna":
    print('Downloading cds')
    download_fna(opt.path, fna_id, opt.version, ncbi_dir, opt.outpath)
elif opt.task == "get_faa":
    print('Downloading faa')
    download_faa(opt.path, faa_id, opt.version, ncbi_dir, opt.outpath)
