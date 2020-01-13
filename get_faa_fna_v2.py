"""Download protein.faa files of strains with Complete or Chromosome assembly level from ftp"""

import os
import random
from os import system
from optparse import OptionParser

def get_assemb(filename, path):
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
def get_data(path, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\t') for s in open(path + files, 'r')]
        outfiles = os.path.join(outpath, filename)
        outfile = open(outfiles, 'w')
        if (len(filelist) - 2) >= 5:
            data = filelist[2:]
            for col in data:
                if col.split('\t')[11] != "Contig" and col.split('\t')[11] != "Scaffold":
                    data2 = col.split('\t')[-3]
                    outfile.write(data2 + '\n')
        outfile.close()
    for files in os.listdir(outpath):
        if os.stat(outpath + files).st_size==0:
            os.remove(outpath + files)

def sampling_5(path, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\n') for s in open(path + files, 'r')]
        if (len(filelist) - 2) >= 5:
            data = random.sample(filelist[:], 5)
            outfiles = os.path.join(outpath, filename + ".txt")
            outfile = open(outfiles, 'w')
            for lines in data:
                line = lines
                outfile.write(line + '\n')
            outfile.close()

def get_faa(path, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\n') for s in open(path + files, 'r')]
        for lines in filelist:
            line = lines.split('/')[-1]
            try:
                os.mkdir(filename)
            except:
                pass
            os.chdir(filename)
            try:
                os.system("wget\t" + lines + '/' + line + "_protein.faa.gz")
            except Exception:
                pass
            os.chdir('..')
            
def get_fna(path, outpath):
    for files in os.listdir(path):
        filename = os.path.splitext(files)[0]
        filelist = [s.strip('\n') for s in open(path + files, 'r')]
        for lines in filelist:
            line = lines.split('/')[-1]
            try:
                os.mkdir(filename)
            except:
                pass
            os.chdir(filename)
            try:
                os.system("wget\t" + lines + '/' + line + "_cds_from_genomic.fna.gz")
            except Exception:
                pass
            os.chdir('..')
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=assembly_summary\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-f : list of bacterial species
\n\t\t\t\t\t-d : directory to save assembly summary files
\t\t\t\t\t=data\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-o : directory to save files
\t\t\t\t\t=sampling\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-o : directory to save files
\t\t\t\t\t=get_faa\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-o : directory to save files
\t\t\t\t\t=get_fna\n
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-d : directory with assembly_summary files
\n\t\t\t\t\t-o : directory to save files""") 
parser.add_option("-f", "--filename", help="List of bacteria obtained from the GenBank")
parser.add_option("-d", "--path", help="Directory with assembly summary files")
parser.add_option("-o", "--outpath", help="Directory for output files")    
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "assembly_summary":
    print('Downloading assembly summary files')
    get_assemb(opt.filename, opt.path)
elif opt.task == "data":
    print('Get complete and scaffold files')
    get_data(opt.path, opt.outpath)
elif opt.task == "sampling":
    print("Sampling")
    sampling_5(opt.path, opt.outpath)
elif opt.task == "get_faa":
    print('Downloading annotated protein files')
    get_faa(opt.path, opt.outpath)
elif opt.task == "get_fna":
    print("Start downloading cds files")
    get_fna(opt.path, opt.outpath)
