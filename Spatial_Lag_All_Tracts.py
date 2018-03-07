from __init__ import *
import pysal as ps
import numpy as np



name_ds = 'Dataset_MAIN/enhanced_dataset.csv'
shapefile = 'Listings shp/MAIN_CT_with_listings/MAIN_tracts_with_listings.shp'
#name_y = 'rent_aff_3'
name_y = 'log_median_rent'
x_columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 22]




ds = ps.open(name_ds, 'r')
print(list(enumerate(ds.header)))
logger.info('Dataset = ' + name_ds)
logger.info('Shapefile = ' + shapefile)

y = ds.by_col(name_y)
y = list(map(float, y))
y = np.array(y).reshape(len(ds), 1)
logger.info('y = ' + name_y)


x = np.zeros((len(ds), 1))
for i, c in enumerate(x_columns):
    data = ds.by_col(ds.header[c])
    data = list(map(float, data))
    data = np.array(data).reshape(len(ds), 1)
    logger.info('Variable #{} :'.format(i+1) + ds.header[c])
    x = np.hstack((x, data))
x = x[:, 1:]



# Weights, row-standarsized
w = ps.knnW_from_shapefile(shapefile, k=4, idVariable=None)
w.transform = 'r'
# Kernel-weights
kw = ps.adaptive_kernelW_from_shapefile(shapefile, k=12, idVariable=None)



## For Spatial Lag Model -- Maximum Likelihood
logger.info('Method = Spatial Lag Model -- Maximum Likelihood')
ml_lag = ps.spreg.ML_Lag(y, x, w, name_y = name_y, name_ds = name_ds)
logger.info('\n'*2 + ml_lag.summary + '\n'*2)
## For Spatial Lag Model -- Maximum Likelihood, with Ord Method
#ml_lag_ord = ps.spreg.ML_Lag(y, x, w, method='ord'); print(ml_lag_ord.summary); logfile.write('\n'*2 + ml_lag_ord.summary + '\n'*2)








