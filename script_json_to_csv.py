import json
import csv
import os



# Vars definitions

path = 'outputs/ios-hw-inventory/'
files = os.listdir(path)

#print(files) #for debugging

for file in files:
    if '.json' in file:
        with open(path+file, 'r') as datain:
            data = json.load(datain)

            f = csv.writer(open(path+file.replace('.json', '.csv'), 'w', newline=''))

            # Write CSV Header, If you dont need that, remove this line
            f.writerow(["name", "description", "pid", "serialnum"])

            # Parsing for json data
            for data in data:
                f.writerow([data["name"],
                            data["description"],
                            data["pid"],
                            data["serialnum"]])
