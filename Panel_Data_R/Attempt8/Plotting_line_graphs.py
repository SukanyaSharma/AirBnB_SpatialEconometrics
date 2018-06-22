#!/usr/bin/env python

'''For plotting line graphs of variables (2010--2016)
'''

# import built-in modules below
import itertools as it
import matplotlib.pyplot as plt

# for tex font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

County = ['Alameda', 'Contra Costa', 'Marin', 'San Francisco', 'San Mateo']
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

MGR = {2016: [1432, 1506, 1764, 1632, 1830],
       2015: [1367, 1426, 1678, 1558, 1728],
       2014: [1325, 1395, 1659, 1533, 1664],
       2013: [1289, 1365, 1628, 1488, 1602],
       2012: [1265, 1340, 1598, 1447, 1541],
       2011: [1228, 1309, 1571, 1388, 1508],
       2010: [1188, 1270, 1523, 1328, 1443]}

MHV = {2016: [593500, 472900, 859400, 858800, 845300],
       2015: [543100, 439900, 815100, 799600, 776300],
       2014: [509300, 417400, 785100, 765700, 736800],
       2013: [493800, 404000, 781900, 744600, 722200],
       2012: [514900, 433800, 810700, 750900, 734100],
       2011: [558300, 490200, 840900, 767300, 763100],
       2010: [590900, 548200, 868000, 785200, 784000]}
       
RB =  {2016: [49.38324349, 52.52582829, 52.10906045, 42.60651271, 45.2690018],
       2015: [49.32112772, 52.76744621, 53.02002839, 42.80808403, 46.3986861],
       2014: [49.66742977, 53.04527248, 53.03132455, 43.88707734, 47.7413631],
       2013: [49.94218203, 52.73021279,	53.18665832, 43.81228591, 48.5304378],
       2012: [50.24741531, 52.93091784,	53.49730178, 43.18337004, 48.3945672],
       2011: [50.00359490, 52.29816588,	51.51126063, 41.71442056, 48.9683786],
       2010: [49.62657710, 51.26231953,	49.80366492, 40.65136207, 48.1756136]}

variables = [MGR, MHV, RB]
variable_names = ['Median gross rent', 'Median house price', 'Rent burdened']

for v in range(3):
    fig = plt.figure(figsize=(7,5))
    ax  = fig.add_subplot(111)
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    
    [plt.plot(year, [variables[v][y][i] for y in year], 'o-', label=County[i]) for i in range(5)]
    plt.ylabel(variable_names[v])
    plt.xlabel('Time in years')
    #plt.grid(True)
    plt.title('{} vs. Time.png'.format(variable_names[v]))
    if v==2:
        ax.legend(loc='upper right')
        plt.ylim(ymax=59)
    elif v==1:
        ax.legend(loc='center right')
        plt.ylim(ymax=950000)
    else:
        ax.legend(loc='lower right')
    plt.savefig('{} vs. Time.png'.format(variable_names[v]), dpi=300)
    
    
fig = plt.figure(figsize=(7,8))

v = 1
ax1 = plt.subplot(311, frameon=False)
plt.suptitle('Affordability trends (2010-2016)', fontsize=16)

[plt.plot(year, [variables[v][y][i] for y in year], 'o-', label=County[i]) for i in range(5)]
plt.setp(ax1.get_xticklabels(), visible=False)
plt.ylabel(variable_names[v])
plt.ylim(ymax=900000-1000)
plt.grid(True)

v = 0
ax2 = plt.subplot(312, sharex=ax1, frameon=False)
[plt.plot(year, [variables[v][y][i] for y in year], 'o-', label=County[i]) for i in range(5)]
plt.setp(ax2.get_xticklabels(), visible=False)
plt.ylabel(variable_names[v])
plt.grid(True)

v = 2
ax3 = plt.subplot(313, sharex=ax1, frameon=False)
[plt.plot(year, [variables[v][y][i] for y in year], 'o-', label=County[i]) for i in range(5)]
plt.ylabel(variable_names[v])
plt.ylim(ymax=54.9)
plt.grid(True)

plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)
'''if v==2:
    ax.legend(loc='upper right')
    plt.ylim(ymax=59)
elif v==1:
    ax.legend(loc='center right')
    plt.ylim(ymax=950000)
else:
    ax.legend(loc='lower right')
'''
plt.xlabel('Time in years')
plt.savefig('Affordability_trends.pdf'.format(variable_names[v]), dpi=300)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
