import pandas as pd
import os, fnmatch

xl = pd.ExcelFile("tin.xlsx")
tin_data = xl.parse("Sheet1")
tin_count=0

tins=tin_data['TIN']
#print(tins)

listOfFiles = os.listdir('./xmls')
#print(listOfFiles)

for entry in listOfFiles:
    for tin in range(len(tins)):
      pattern = str(tins[tin]) + ".xml"
      if fnmatch.fnmatch(entry, pattern):
          #the following logic moves the sorted files from the xmls folder to a new directory called sorted
          os.rename('./xmls/' + pattern, './sorted/' + pattern)
          tin_count = tin_count + 1

print(tin_count , " number of xml files in xmls directory where found corresponding to the excel file TIN column and moved to the sorted folder ")

