import pysal as ps
import numpy as np

db = ps.open('Dataset_MAIN/enhanced_dataset.csv', 'r')
print(list(enumerate(db.header)))


rent_aff_1 = db.by_col('rent_aff_1')
rent_aff_1 = list(map(float, rent_aff_1))
y = np.array(rent_aff_1).reshape(len(db), 1); print('y = rent_aff_1')


columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21]

x = np.zeros((len(db), 1))

for i, c in enumerate(columns):
    data = db.by_col(db.header[c])
    data = list(map(float, data))
    data = np.array(data).reshape(len(db), 1)    
    print('Variable #{} :'.format(i+1), db.header[c])
    x = np.hstack((x, data))
x = x[:, 1:]



# Weights, row-standarsized
w = ps.knnW_from_shapefile('Listings shp/MAIN_CT_with_listings/MAIN_tracts_with_listings.shp', k=4, idVariable=None)
w.transform = 'r'
# Kernel-weights
kw = ps.adaptive_kernelW_from_shapefile('Listings shp/MAIN_CT_with_listings/MAIN_tracts_with_listings.shp', k=12, idVariable=None)








logfile = open('Results.log', 'a')

## For Spatial Lag Model -- Maximum Likelihood
ml_lag = ps.spreg.ML_Lag(y, x, w); print(ml_lag.summary); logfile.write('\n'*2 + ml_lag.summary + '\n'*2)
## For Spatial Lag Model -- Maximum Likelihood, with Ord Method
ml_lag_ord = ps.spreg.ML_Lag(y, x, w, method='ord'); print(ml_lag_ord.summary); logfile.write('\n'*2 + ml_lag_ord.summary + '\n'*2)

logfile.close()









