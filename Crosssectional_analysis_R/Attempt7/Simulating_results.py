
# coding: utf-8

# # We will simulate the cross-sectional spatial lag result.    
#     Y = [Rent burdened, Rent overburdened, Median rent, Median house price]
#     X = [Percent Airbnb, Weighted Airbnb listings]

# In[1]:


import numpy as np
#%matplotlib notebook
import itertools as it
import matplotlib.pyplot as plt
from math import e, log


# In[2]:


Y_names = ['Rent burdened', 'Rent overburdened', 'Median rent', 'Median house price']
Y_means = [3.7518, 2.97587, 7.3223, 13.06562]       # these are for log values

X_names = ['Percent Airbnb', 'Weighted Airbnb listings']
X_means = [10.27940, 15.48]                         # these are for normal values
X_std   = [17.54471, 30.67383]                      # these are for normal values

YX_names = list(it.product(Y_names, X_names))
YX_means = list(it.product(Y_means, X_means))
X_std    = 4*X_std
print(YX_names)
print(X_std)

coeffs = [0.001, 0.021,
          0.026, 0.013,
          0.071, 0.142,
          0.181, 0.223]     # these are for log-log values

c = [YX_means[i][0] - coeffs[i]*log(YX_means[i][1]) for i in range(8)]
k = [e**i for i in c]
k


# In[4]:


def y(i, x): return k[i]*x**coeffs[i]

for i in range(8):
    xs = [YX_means[i][1] + j*(X_std[i]) for j in range(0,4)]
    ys = [y(i,x) for x in xs]
    print(YX_names[i])
    plt.plot(xs, ys, 'o-', label=str(YX_names[i]))
    plt.show()

