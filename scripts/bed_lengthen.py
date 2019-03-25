import pandas as pd
import sys

# this script is used to filter out peaks that are shorter than 100
# python bed_lengthen.py input.bed out.bed

bed = pd.read_csv(sys.argv[1], sep='\t', names=['chr', 'start', 'end'])
res = bed[(bed['end'] - bed['start']) > 100]
res.to_csv(sys.argv[2], sep='\t', header=False, index=False)
