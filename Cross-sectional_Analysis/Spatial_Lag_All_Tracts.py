from __init__All_Tracts import *
import pysal as ps
import numpy as np



name_ds = '../Dataset_MAIN/all_data_all_tracts.csv'
shapefile = '../Dataset_MAIN/Listings_shp/MAIN_CT_All/ALL_TRACTS_ALL_DATA.shp'
names_y = ['rent_aff_1', 'rent_aff_2', 'rent_aff_3', 'log_median_rent', 'log_median_house_price']

x_columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 23]  # 21 = Airbnb_all_rentals
#x_columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 22, 23]  # 22 = Airbnb_active_rentals



ds = ps.open(name_ds, 'r')
print(list(enumerate(ds.header)))
logger.info('Dataset = ' + name_ds)
logger.info('Shapefile = ' + shapefile)


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
name_w = shapefile.split('/')[-1]
# Kernel-weights
kw = ps.adaptive_kernelW_from_shapefile(shapefile, k=12, idVariable=None)


for name_y in names_y:
    y = ds.by_col(name_y)
    y = list(map(float, y))
    y = np.array(y).reshape(len(ds), 1)
    logger.info('y = ' + name_y)

    ## For Spatial Lag Model -- Maximum Likelihood
    logger.info('Method = Spatial Lag Model -- Maximum Likelihood')
    ml_lag = ps.spreg.ML_Lag(y, x, w, name_y = name_y, name_ds = name_ds, name_w = name_w)
    logger.info('\n'*2 + ml_lag.summary + '\n'*23)
    







