#!/usr/bin/env python

'''Why is the std. dev. larger than the mean?
'''

# import built-in modules below
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import log

with open('Looking_at_data_vaibhav.csv', 'r') as readfile:
    header = readfile.readline()
    lines = [line.strip().split(',') for line in readfile]
    aa = [float(i[0]) for i in lines]
    ac = [float(i[1]) for i in lines]

print(np.mean(aa), np.std(aa))
print(np.mean(ac), np.std(ac))
ac_log = [log(i) for i in ac]
sns.distplot(ac_log)
plt.show()
