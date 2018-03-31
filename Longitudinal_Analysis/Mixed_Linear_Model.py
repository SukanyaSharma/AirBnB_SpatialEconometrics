from __init__Longitudinal import *
import numpy as np
import pandas as pd
import statsmodels.api as sm



db = 'Dataset_MAIN/Longitudinal Analysis Dataset/Panel_Data.csv'
logger.info('Database: ' + db)
data = pd.read_csv('../' + db)
data2 = np.asarray(data)


ys = data.columns[3:7]

for x in [7, 8]:
    for y in ys:
        fml = y + ' ~ ' + data.columns[x] + ' + ' + ' + '.join(data.columns[9:18])
        logger.info('Formula:\n\t\t' + fml)
        logger.info('Groups: Census_Tract')

        model = sm.MixedLM.from_formula(fml,
                                        data,
                                        groups = data['Census_Tract'])
    
        result = model.fit()
        logger.info('\n'*3 + str(result.summary()))

