import numpy as np


years = ['', ' (copy)'] #['2013', '2014', '2015', '2016', '2017']
filename = '../Dataset_MAIN/enhanced_dataset'
ct = 196 # number of census tracts. Must match number of rows-1 in datafile.


f = {y: open(filename + y + '.csv', 'r') for y in years}
g = open('Consolidated.csv', 'w')

[f[y].readline() for y in years] # skips headers line


for counter in range(ct):
    for y in years:
        line = y + ',' + f[y].readline()
        g.write( line )




[i.close() for i in f.values()]
g.close()
