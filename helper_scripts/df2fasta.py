#!/usr/bin/env python3

import sys
import pandas as pd
infile = sys.argv[1]

#Write fasta file from given dataframe and filename

def write_fasta(name, df):
    with open(name + ".fa", "w") as out:
        for i in range(len(df)):
            out.write('>' + df.Name[i] + '\n')
            sequence = df.Sequence[i]
            # Write sequence in lines of 60 characters
            for j in range(0, len(sequence), 60):
                out.write(sequence[j:j+60] + '\n')
 

read_df = pd.read_csv(infile)
write_fasta(infile[:-4], read_df)
