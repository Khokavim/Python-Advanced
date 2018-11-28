

import pandas as pd
import numpy as np

data = pd.read_csv('phone.csv', delimiter=",", names=['name','age','salary','origin'])
#print(data)
print(np.mean(data['age']))
