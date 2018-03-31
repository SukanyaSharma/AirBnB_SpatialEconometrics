import numpy as np

with open('School_outcome_without_missing_calc.csv','r') as readfile:
    header=readfile.readline()
    data=readfile.readlines()
data= [line.split(',') for line in data]

tract_info= {line[0] : [] for line in data}
for line in data :
    tract_info[line[0]].append(line[1:3])

for tract in tract_info.keys():
    tract_info[tract] = sorted(tract_info[tract], key = lambda i: i[1])[0]
    
#[print(tract, tract_info[tract])  for tract in sorted(tract_info)]

with open('score_generation.csv','w') as writefile:
    writefile.write(header)
    [writefile.write(tract + ',' + ','.join(tract_info[tract])+'\n') for tract in sorted(tract_info)]