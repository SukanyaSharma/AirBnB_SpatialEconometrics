####################################################
## Y = rent_burdened
## X = [airbnb_all_rentals, airbnb_active_rentals]
####################################################

data = read.csv('all_data_all_tracts.csv')

library(spdep)
library(car)
library(stargazer)
library(maptools)

attach(data)
Y <- cbind(rent_burdened)


# X = airbnb_all_rentals
X_old <- cbind(log_BART_dist,
               log_CBD_dist,
               coastal_tracts_dummy,
               percent_unempl,
               percent_non_white,
               percent_foreign_born,
               log_MHI,
               percent_airbnb_all_rentals,
               School_district_quality,
               job_acc_auto,
               job_acc_transit)
mat <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot (we remove log_MHI)
X = cbind(log_BART_dist,
          log_CBD_dist,
          coastal_tracts_dummy,
          percent_unempl,
          percent_non_white,
          percent_foreign_born,
          percent_airbnb_all_rentals,
          School_district_quality,
          job_acc_auto,
          job_acc_transit)
mat <- cor(X)
spm(X)

# Regression (defauls to OLS)
reg1 <- lm(rent_burdened ~ log_BART_dist
                           + log_CBD_dist
                           + coastal_tracts_dummy
                           + percent_unempl
                           + percent_non_white
                           + percent_foreign_born
                           + percent_airbnb_all_rentals
                           + School_district_quality
                           + job_acc_auto
                           + job_acc_transit)
stargazer(reg1)

# Variance inflation factor: checking for multicollinearity
vif(reg1)
stargazer(vif(reg1))

# Creating neighbors through shapefile
shpfile = readShapePoly('All_Tracts_Only_Land_v3/All_Tracts_Only_Land_v3.shp')
lat <- matrix(shpfile$INTPTLAT)
lat <- mapply(lat, FUN = as.numeric)
lat <- matrix(lat)
long <- matrix(shpfile$INTPTLON)
long <- mapply(long, FUN = as.numeric)
long <- matrix(long)              
coords <- cbind(long, lat)
neighbors <- poly2nb(shpfile)
summary(neighbors)
plot(neighbors, coords)
#neighbors[[177]] = NULL # removing island with no links from list of neighbors

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)
# Moran's I test (error on this section)
# ===========================================
moran.test(rent_burdened, listw)
moran.plot(rent_burdened, listw)
# ===========================================

#Spatial Lag Model
spatial.lag <- lagsarlm(rent_burdened ~ log_BART_dist
                                        + log_CBD_dist
                                        + coastal_tracts_dummy
                                        + percent_unempl
                                        + percent_non_white
                                        + percent_foreign_born
                                        + percent_airbnb_all_rentals
                                        + School_district_quality
                                        + job_acc_auto
                                        + job_acc_transit,
                        data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(rent_burdened ~ log_BART_dist
                                            + log_CBD_dist
                                            + coastal_tracts_dummy
                                            + percent_unempl
                                            + percent_non_white
                                            + percent_foreign_born
                                            + percent_airbnb_all_rentals
                                            + School_district_quality
                                            + job_acc_auto
                                            + job_acc_transit,
                            data = data, listw)
summary(spatial.error)
stargazer(spatial.error)


############################################################################

# X = airbnb_active_rentals
X_old <- cbind(log_BART_dist,
               log_CBD_dist,
               coastal_tracts_dummy,
               percent_unempl,
               percent_non_white,
               percent_foreign_born,
               log_MHI,
               percent_airbnb_active_rentals,
               School_district_quality,
               job_acc_auto,
               job_acc_transit)
mat <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot (we remove log_MHI)
X = cbind(log_BART_dist,
          log_CBD_dist,
          coastal_tracts_dummy,
          percent_unempl,
          percent_non_white,
          percent_foreign_born,
          percent_airbnb_active_rentals,
          School_district_quality,
          job_acc_auto,
          job_acc_transit)
mat <- cor(X)
spm(X)

# Regression (defauls to OLS)
reg1 <- lm(rent_burdened ~ log_BART_dist
           + log_CBD_dist
           + coastal_tracts_dummy
           + percent_unempl
           + percent_non_white
           + percent_foreign_born
           + percent_airbnb_active_rentals
           + School_district_quality
           + job_acc_auto
           + job_acc_transit)
stargazer(reg1)

# Variance inflation factor: checking for multicollinearity
vif(reg1)
stargazer(vif(reg1))

# Creating neighbors through shapefile
shpfile = readShapePoly('All_Tracts_Only_Land_v3/All_Tracts_Only_Land_v3.shp')
lat <- matrix(shpfile$INTPTLAT)
lat <- mapply(lat, FUN = as.numeric)
lat <- matrix(lat)
long <- matrix(shpfile$INTPTLON)
long <- mapply(long, FUN = as.numeric)
long <- matrix(long)              
coords <- cbind(long, lat)
neighbors <- poly2nb(shpfile)
summary(neighbors)
plot(neighbors, coords)
#neighbors[[177]] = NULL # removing island with no links from list of neighbors

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)
# Moran's I test (error on this section)
# ===========================================
moran.test(rent_burdened, listw)
moran.plot(rent_burdened, listw)
# ===========================================

#Spatial Lag Model
spatial.lag <- lagsarlm(rent_burdened ~ log_BART_dist
                                        + log_CBD_dist
                                        + coastal_tracts_dummy
                                        + percent_unempl
                                        + percent_non_white
                                        + percent_foreign_born
                                        + percent_airbnb_active_rentals
                                        + School_district_quality
                                        + job_acc_auto
                                        + job_acc_transit,
                        data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(rent_burdened ~ log_BART_dist
                            + log_CBD_dist
                            + coastal_tracts_dummy
                            + percent_unempl
                            + percent_non_white
                            + percent_foreign_born
                            + percent_airbnb_all_rentals
                            + School_district_quality
                            + job_acc_auto
                            + job_acc_transit,
                            data = data, listw)
summary(spatial.error)
stargazer(spatial.error)



