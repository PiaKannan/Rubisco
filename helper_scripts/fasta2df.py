#!/usr/bin/env python3

"""
@author: Priya
"""
#import required modules
import sys
import pandas as pd
import numpy as np

#Read fastafile from folder and convert it to dataframe of columns [id, sequence]
def read(file):
    fasta = open(file,"r")
    dic={}
    #dictionary helps in removing duplicate keys
    for line in fasta:
        line =line.strip()
        if line[0] == ">":
            header = line[1:].split(' ')[0]
            dic[header] = ""
        else:
            data = line
            dic[header] += data
    return pd.DataFrame({'Name' : dic.keys() , 'Sequence' : dic.values() })

ifile = sys.argv[1]
ofile = ifile.split('.')[0]+'.csv'
df=read(ifile)
df.to_csv(ofile,index=False)

