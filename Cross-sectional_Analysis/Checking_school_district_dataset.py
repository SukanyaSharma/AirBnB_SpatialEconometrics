path = '/media/vaibhav/Work/Sukanya/Spatial_Econometrics/Dataset_MAIN/School_District_Quality/'
with open(path + 'CT_Centroid_outcome.csv', 'r') as inputfile:
    inputfile.readline()
    tracts = inputfile.readlines()

tracts = [line.split(',')[0] for line in tracts]

with open(path + 'School_outcome.csv', 'r') as checkfile:
    checkfile.readline()
    info  = checkfile.readlines()

info  = [line.split(',') for line in info]
info  = {line[0]: line for line in info}


missing = []
for i in tracts:
    if i not in info.keys():
        missing.append(i)
    elif info[i][3] == '' or info[i][3] == '0':
        missing.append(i)

[print(i + ',0,0') for i in missing]
