import json
import csv
import os



# Vars definitions

path = '/home/pdiazd/ansible-network/outputs/health-check/'
files = os.listdir(path)

print(files) #for debugging

for file in files:
    if '.json' in file:
        with open(path+file, 'r') as datain:
            data = json.load(datain)

            f = csv.writer(open(path+file.replace('.json', '.csv'), 'w', newline=''))

            # Write CSV Header
            f.writerow(["hostname", "interface", "admin status", "line protocol", "input rate (bps)", "input rate (pps)", "output rate (bps)", "output rate (pps)", "input errors", "CRC", "output errors", "interface resets" ])

            # Parsing for json data
            for data in data:
                f.writerow([data["hostname"],
                            data["interface_name"],
                            data["admin_status"],
                            data["line_protocol"],
                            data["input_rate_bps"],
                            data["input_rate_pps"],
                            data["output_rate_bps"],
                            data["output_rate_pps"],
                            data["input_errors"],
                            data["crc"],
                            data["output_errors"],
                            data["interface_resets"]])
