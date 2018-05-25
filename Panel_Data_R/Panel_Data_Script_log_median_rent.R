library(splm)
library(spdep)
library(plm)
library(Ecdat)
library(stargazer)


data <- read.csv('Panel_Data.csv')
attach(data)
summary(data)

Y <- cbind(log_median_rent)
X <- cbind(log_MHI, percent_airbnb_all_rentals, percent_bachelors_degree,
           percent_foreign_born, percent_unempl)

# Setting data as panel data
pdata <- plm.data(data, indexes = c('Id', 't'))

# descriptive statistics
summary(Y)
summary(X)

# Pooled OLS Estimator

pooling <- plm(Y ~ X, data = pdata, model = 'pooling')
summary(pooling)
stargazer(pooling)

# Between estimator

between <- plm(Y ~ X, data = pdata, model = 'between')
summary(between)
stargazer(between)

# First differences estimator

fd <- plm(Y ~ X, data = pdata, model = 'fd')
summary(fd)
stargazer(fd)

# Fixed Effects or within estimator

within <- plm(Y ~ X, data = pdata, model = 'within')
summary(within)
stargazer(within)


# Random Effects

random <- plm(Y ~ X, data = pdata, model = 'random')
summary(random)
stargazer(random)

# LM test for random effects vs OLS

plmtest(pooling)

# LM Test for fixed effects vs OLS

pFtest(within, pooling)

# Hausman test for fixed vs random effects model

phtest(random, within)
