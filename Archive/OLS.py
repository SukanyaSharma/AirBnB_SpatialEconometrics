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


model = ps.spreg.OLS(y, x)
print('R-squared =', model.r2)

logfile.write('\n'*2 + model.summary + '\n'*2)


## For non-spatial OLS testing
ols_full = ps.spreg.OLS(y, x, w=None, robust=None, gwk=None, sig2n_k=True, nonspat_diag=True, spat_diag=False, moran=False, white_test=False, vm=False, name_y=None, name_x=None, name_w=None, name_gwk=None, name_ds=None)
print(ols_full.summary)

logfile.write('\n'*2 + ols_full.summary + '\n'*2)

## For OLS + White-test
ols2 = ps.spreg.OLS(y, x, w=None, robust=None, gwk=None, sig2n_k=True, nonspat_diag=True, spat_diag=False, moran=False, white_test=True, vm=False, name_y=None, name_x=None, name_w=None, name_gwk=None, name_ds=None)
print(ols2.summary)

logfile.write('\n'*2 + ols2.summary + '\n'*2)
logfile.close()

