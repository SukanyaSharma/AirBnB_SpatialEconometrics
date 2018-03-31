import numpy as np
import pandas as pd
import statsmodels.api as sm

#with open('../Dataset_MAIN/Longitudinal Analysis Dataset/Panel_Data.csv', 'r') as readfile:
#    header = readfile.readline()
#    data = readfile.readlines()

#data = [i.split(',') for i in data]

#for i in range(20):
#    if i != 0 and i != 2:
#        print(list(map(float, data[:][i])))
#        break
#        data[:,i] = list(map(float, data[:,i]))


data = pd.read_csv('../Dataset_MAIN/Longitudinal Analysis Dataset/Panel_Data.csv')
data2 = np.asarray(data)

fml = 'rent_aff_1 ~ ' + ' + '.join(data.columns[7:18])

#model = sm.MixedLM(endog = np.array(data['rent_aff_1']),\
#                   exog = np.array(data2[:, 7:18]),\
#                   groups = data['Census_Tract'],\
#                   exog_re=None)

model = sm.MixedLM.from_formula(fml,\
                                data,
                                groups = data['Census_Tract'])

result = model.fit()
print(result.summary())
print(dir(result))
