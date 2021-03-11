import os
import pandas as pd
import glob
import time

#Global vars
os.chdir("outputs/ios-hw-inventory/")
timestr = time.strftime("%Y%m%d")

#Search for files with .csv extension
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#Combine all .csv files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#Export to csv
combined_csv.to_csv("full-reports/ios-hw-inventory_report-"+timestr+".csv", index=False, encoding='utf-8-sig')
