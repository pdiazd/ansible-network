import pandas as pd
import csv
import re
import os

path = '/home/eve/Ansible/outputs/health-check/'
files = os.listdir(path)

sh_log= '(.|\n)*sh\S*\s+log\S*\s*.*?\S{3}\s{1,2}\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}((.|\n)*?#)'
pDates = '(\S{3})\s{1,2}(\d{1,2})\s(\d{1,2}):\d{1,2}:\d{1,2}'
pNames = ':\s*%(.*?):'   #Not greedy
names = []
cols = []

for file in files:
    if 'log' and '.txt' in file:
        #
        datain = open(path+file, 'r')
        Lines = datain.readlines()
        for linea in Lines:
            matchName = re.search(pNames, linea)
            matchDate = re.search(pDates, linea)
            if (matchName):
                if matchName[1] not in names:
                    names.append(matchName[1])
            if (matchDate):
                col = ('2021-'+matchDate[1]+'-'+matchDate[2]+'-'+matchDate[3])
                if col not in cols:
                    cols.append(col)
        #              
        df = pd.DataFrame(0, index=range(len(names)), columns=range(len(cols)))
        df.columns=cols
        df.index=names
        df = df.rename_axis(index='name', columns=None)
        #
        for linea in Lines:  
            m1 = re.search(pNames, linea)
            m2 = re.search(pDates, linea)
            if (m1 and m2):
                nombre = m1[1]
                fecha = ('2021-'+m2[1]+'-'+m2[2]+'-'+m2[3])
                oldValue=df.at[nombre,fecha]        
                df.loc[nombre,fecha] = oldValue+1
        #
        file_out = file.replace('log', 'out')
        df.to_csv(path+file_out ,sep='\t')
