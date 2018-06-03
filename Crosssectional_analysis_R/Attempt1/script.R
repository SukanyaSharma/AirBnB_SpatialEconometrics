data = read.csv('all_data_all_tracts.csv')

library(spdep)
library(car)
library(stargazer)
library(maptools)

attach(data)
Y <- cbind(rent_burdened)
X_old <- cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_unempl, percent_non_white,
           percent_foreign_born, log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat <- cor(X)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot
X = cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_non_white,
          log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat <- cor(X)
spm(X)

# Regression
reg1 <- lm(rent_burdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy
           + percent_non_white + log_MHI +  percent_airbnb_all_rentals
           + School_district_quality)
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

# OLS regression
olsreg <- lm(Y ~ X)
stargazer(olsreg)

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)
# Moran's I test (error on this section)
# ===========================================
moran.test(rent_burdened, listw)
moran.plot(rent_burdened, listw)
# ===========================================

# Spatial weights matrix based on distance
#nb <- dnearneigh(cbind(long,lat), d1=0, d2=10)
#nb <- knearneigh(cbind(long,lat), k = 4)
#listw <- nb2listw(nb, style = "W")
#summary(listw)

# Moran's I test
#moran.test(Y, listw)

# Lagrangian multiplier test for spatial lag and spatial error dependencies
#lm.LMtests(olsreg, listw, test = c('LMlag', 'LMerr'))

#Spatial Lag Model
spatial.lag <- lagsarlm(rent_burdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                        percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(rent_burdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                              percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.error)
stargazer(spatial.error)

#=========================================================
#=========================================================
#=========================================================
#change of variables
## y = rent_overburdened
## change in X = airbnb_all_rentals
Y2 <- cbind(rent_overburdened)
X_old <- cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_unempl, percent_non_white,
               percent_foreign_born, log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat2 <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot
X = cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_non_white,
          log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat <- cor(X)
spm(X)

# Regression
reg2 <- lm(rent_overburdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy
           + percent_non_white + log_MHI +  percent_airbnb_all_rentals
           + School_district_quality)
stargazer(reg2)

# Variance inflation factor: checking for multicollinearity
vif(reg2)
stargazer(vif(reg2))

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

# OLS regression
olsreg <- lm(Y ~ X)
stargazer(olsreg)

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)
# Moran's I test (error on this section)
# ===========================================
moran.test(rent_overburdened, listw)
moran.plot(rent_overburdened, listw)
# ===========================================

# Spatial weights matrix based on distance
#nb <- dnearneigh(cbind(long,lat), d1=0, d2=10)
#nb <- knearneigh(cbind(long,lat), k = 4)
#listw <- nb2listw(nb, style = "W")
#summary(listw)

# Moran's I test
#moran.test(Y, listw)

# Lagrangian multiplier test for spatial lag and spatial error dependencies
#lm.LMtests(olsreg, listw, test = c('LMlag', 'LMerr'))

#Spatial Lag Model
spatial.lag <- lagsarlm(rent_overburdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                          percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(rent_overburdened ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                              percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.error)
stargazer(spatial.error)

#=========================================================
#=========================================================
#=========================================================
#change of variables
## y = log_median_rent
## change in X = airbnb_all_rentals
Y3 <- cbind(log_median_rent)
X_old <- cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_unempl, percent_non_white,
               percent_foreign_born, log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat2 <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot
X = cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_non_white,
          log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat <- cor(X)
spm(X)

# Regression
reg3<- lm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy
           + percent_non_white + log_MHI +  percent_airbnb_all_rentals)
stargazer(reg3)

# Variance inflation factor: checking for multicollinearity
vif(reg3)
stargazer(vif(reg3))

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

# OLS regression
olsreg <- lm(Y ~ X)
stargazer(olsreg)

# Spatial analysis based in contiguity
# Spatial weight matrix
#listw <- nb2listw(neighbors)
# Moran's I test (error on this section)
# ===========================================
moran.test(log_median_rent, listw)
moran.plot(log_median_rent, listw)
# ===========================================

# Spatial weights matrix based on distance
#nb <- dnearneigh(cbind(long,lat), d1=0, d2=10)
#nb <- knearneigh(cbind(long,lat), k = 5)
#listw <- nb2listw(nb, )
#summary(listw)

# Moran's I test
#moran.test(Y, listw)

# Lagrangian multiplier test for spatial lag and spatial error dependencies
#lm.LMtests(olsreg, listw, test = c('LMlag', 'LMerr'))

#Spatial Lag Model
spatial.lag <- lagsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                          percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                              percent_non_white + log_MHI + percent_airbnb_all_rentals, data = data, listw)
summary(spatial.error)
stargazer(spatial.error)


#=========================================================
#=========================================================
#=========================================================
#change of variables
## y = log_median_rent
## change in X = airbnb_active_rentals
Y4 <- cbind(log_median_rent)
X_old <- cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_unempl, percent_non_white,
               percent_foreign_born, log_MHI, percent_airbnb_active_rentals, School_district_quality)
mat2 <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot
X = cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_non_white,
          log_MHI, percent_airbnb_active_rentals, School_district_quality)
mat <- cor(X)
spm(X)

# Regression
reg4<- lm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy
          + percent_non_white + log_MHI +  percent_airbnb_active_rentals)
stargazer(reg4)

# Variance inflation factor: checking for multicollinearity
vif(reg4)
stargazer(vif(reg4))

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

# OLS regression
olsreg <- lm(Y ~ X)
stargazer(olsreg)

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)


# Moran's I test (error on this section)
# ===========================================
moran.test(log_median_rent, listw)
moran.plot(log_median_rent, listw)
# ===========================================

# Spatial weights matrix based on distance
#nb <- dnearneigh(cbind(long,lat), d1=0, d2=10)
#nb <- knearneigh(cbind(long,lat), k = 5)
#listw <- nb2listw(nb, )
#summary(listw)

# Moran's I test
#moran.test(Y, listw)

# Lagrangian multiplier test for spatial lag and spatial error dependencies
#lm.LMtests(olsreg, listw, test = c('LMlag', 'LMerr'))

#Spatial Lag Model
spatial.lag <- lagsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                          percent_non_white + log_MHI + percent_airbnb_active_rentals, data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                              percent_non_white + log_MHI + percent_airbnb_active_rentals, data = data, listw)
summary(spatial.error)
stargazer(spatial.error)

#=========================================================
#=========================================================
#=========================================================
#change of variables
## y = rent_hourly wage
## change in X = airbnb_all_rentals
Y5 <- cbind(rent_hourly_wage)
X_old <- cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_unempl, percent_non_white,
               percent_foreign_born, log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat2 <- cor(X_old)
print(mat)

# Scatter Plot Matrix
spm(X_old)

# Redefining X after looking at scatterplot
X = cbind(log_BART_dist, log_CBD_dist, coastal_tracts_dummy, percent_non_white,
          log_MHI, percent_airbnb_all_rentals, School_district_quality)
mat <- cor(X)
spm(X)

# Regression
reg5<- lm(rent_hourly_wage~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy
          + percent_non_white + log_MHI +  percent_airbnb_all_rentals)
stargazer(reg5)

# Variance inflation factor: checking for multicollinearity
vif(reg5)
stargazer(vif(reg5))

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

# OLS regression
olsreg <- lm(Y ~ X)
stargazer(olsreg)

# Spatial analysis based in contiguity
# Spatial weight matrix
listw <- nb2listw(neighbors)


# Moran's I test (error on this section)
# ===========================================
moran.test(rent_hourly_wage, listw)
moran.plot(rent_hourly_wage, listw)
# ===========================================

# Spatial weights matrix based on distance
#nb <- dnearneigh(cbind(long,lat), d1=0, d2=10)
#nb <- knearneigh(cbind(long,lat), k = 5)
#listw <- nb2listw(nb, )
#summary(listw)

# Moran's I test
#moran.test(Y, listw)

# Lagrangian multiplier test for spatial lag and spatial error dependencies
#lm.LMtests(olsreg, listw, test = c('LMlag', 'LMerr'))

#Spatial Lag Model
spatial.lag <- lagsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                          percent_non_white + log_MHI + percent_airbnb_active_rentals, data = data, listw)
summary(spatial.lag)
stargazer(spatial.lag)

#Spatial Error Model
spatial.error <- errorsarlm(log_median_rent ~ log_BART_dist + log_CBD_dist + coastal_tracts_dummy +
                              percent_non_white + log_MHI + percent_airbnb_active_rentals, data = data, listw)
summary(spatial.error)
stargazer(spatial.error)