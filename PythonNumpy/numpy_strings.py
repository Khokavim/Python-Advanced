import numpy as np
import random

personals = np.array(['Meshach', 'Daniel', 'Hameed', 'Esther', 'Suzan', 'Cole', 'Paul'])
print (personals == 'Meshach')
#checks for the string 'Manu' in personals. If present it returns true; else false#

algebra = random.randint(1,100)# empty will return a matrix of size 7,4
for j in range(100):
    algebra[j] = j
algebra
