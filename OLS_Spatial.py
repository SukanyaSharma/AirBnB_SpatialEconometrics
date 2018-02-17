import pysal as ps
import numpy as np

db = ps.open('MasterTable_Airbnb.csv', 'r')
print(list(enumerate(db.header)))

median_rent = db.by_col('Median Gross Rent')
for i in range(len(median_rent)):
    if median_rent[i] == 'NA':
        median_rent[i] = 10**50

        
median_rent = list(map(float, median_rent))
y = np.array(median_rent).reshape(len(db), 1)
y = np.log(y); print('y = log(Median Gross Rent)')

columns = [1, 2, 3, 6, 7, 8, 11]
log_variables = {c: False for c in columns}
log_variables[11] = True

x = np.zeros((len(db), 1))
for i, c in enumerate(columns):
    data = db.by_col(db.header[c])
    for entry_number in range(len(data)):
        if data[entry_number] == '':
            data[entry_number] = 0.0
    data = list(map(float, data))
    data = np.array(data).reshape(len(db), 1)    
    if log_variables[c]:
        data = np.log(data)
        print('Variable #{} :'.format(i+1), 'log({})'.format(db.header[c]))
    else:
        print('Variable #{} :'.format(i+1), db.header[c])
    x = np.hstack((x, data))
x = x[:, 1:]

logfile = open('Results.log', 'a')



# Weights, row-standarsized
w = ps.knnW_from_shapefile('Listings shp/Tract_With_Airbnb.shp', k=4, idVariable=None)
w.transform = 'r'

# Kernel-weights
kw = ps.adaptive_kernelW_from_shapefile('Listings shp/Tract_With_Airbnb.shp', k=12, idVariable=None)

## For OLS + White-test + Spatial Diagnostics
ols_spat = ps.spreg.OLS(y, x, w=w, robust=None, gwk=kw, sig2n_k=True, nonspat_diag=False, spat_diag=True, moran=True, white_test=True, vm=False, name_y=None, name_x=None, name_w=None, name_gwk=None, name_ds=None)
#print(ols_spat.summary)

#logfile.write('\n'*2 + ols_spat.summary + '\n'*2)
logfile.close()

## Langrange Multiplier error and lag values.
vw = ps.spreg.diagnostics_sp.LMtests(ols_spat, w)
print(vw)
print(vw.lme)
print(vw.lml)
