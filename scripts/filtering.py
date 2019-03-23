#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import sys

# this script is used to filter fold change atac bed files for DEP

df = pd.read_csv(sys.argv[1], sep='\t', names=['chr', 'start', 'end', 'value'])
df_filtered = df[(df['value'] > float(sys.argv[2])) | (df['value'] < -float(sys.argv[2]))]
df_filtered = df_filtered.reset_index()
df_filtered.to_csv(sys.argv[3], header=False, sep='\t', index=False, float_format='%.7f',
                   columns=['chr', 'start', 'end', 'index', 'value'])
