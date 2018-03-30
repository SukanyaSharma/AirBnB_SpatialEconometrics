import numpy as np


years = ['2013', '2014', '2015', '2016']
filename = '../Dataset_MAIN/Longitudinal Analysis Dataset/{}_combined.csv'
sf_tracts = '../Dataset_MAIN/Longitudinal Analysis Dataset/SF_CT_List.csv'
ct = 976 # number of census tracts. Must match number of rows-1 in datafile.


sf_tracts = list(open(sf_tracts, 'r'))[1:]
sf_tracts = [i[:-1] for i in sf_tracts]
print(sf_tracts)
f = {y: open(filename.format(y), 'r') for y in years}
g = open('../Dataset_MAIN/Longitudinal Analysis Dataset/Panel_Data.csv', 'w')

[f[y].readline() for y in years] # skips headers line


for counter in range(ct):
    for y in years:
        line = y + ',' + f[y].readline()
        tract = line.split(',')[2]
        if tract in sf_tracts:
            g.write( line )



[i.close() for i in f.values()]
g.close()
