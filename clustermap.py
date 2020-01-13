"""Clustermap analysis of pangenome
Input: proteinortho file transformed into binary (0,1)
Output: fig"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from optparse import OptionParser

#pd.set_option('display.max_columns', col) #unique for each file
#pd.set_option('display.max_rows', row) #unique for each file
def cluster(path, outpath):
    df_csv = pd.read_csv(path)

    h = 150 #height for fig size - optional
    w = 100 #width for fig size - optional
    df_clust = sns.clustermap(df_csv, method='complete', col_cluster=True, xticklabels=True, figsize=(w, h), vmin=1, vmax=0)
    df_clust.savefig(outpath)
parser = OptionParser()
parser.add_option("-t", "--task", help="""task code:\n\t\t\t\t\t
=clustermap\n\r
\n\t\t\t\t\tRequired option:
\n\t\t\t\t\t-p : path to the matrix file
\n\t\t\t\t\t-o : outpath to save fig""") 
parser.add_option("-p", "--path", help="Path to the matrix file")
parser.add_option("-o", "--outpath", help="Path to save plot")    
opt, args = parser.parse_args()
print(opt.task)
if opt.task == "clustermap":
    print('Clustermap analysis')
    cluster(opt.path, opt.outpath)
