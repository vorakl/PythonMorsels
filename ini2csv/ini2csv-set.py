#usr/bin/env python3

import configparser
import sys
import csv

if sys.argv[1] == '--collapsed':
    collapsed = True
    in_file = sys.argv[2]
    out_file = sys.argv[3]
else:
    collapsed = False
    in_file = sys.argv[1]
    out_file = sys.argv[2]

config = configparser.ConfigParser()
config.read(in_file)

with open(out_file, 'wt', newline='') as csv_file:
    if not collapsed:
        config_rows = ([section, k, v] for section in config.sections()
                                       for k, v in config[section].items())
        csvwr = csv.writer(csv_file)
        csvwr.writerows(config_rows)
    else:
        field_row = {'header'}
        config_rows = []
        for section in config.sections():
            tmp_row = {'header':section}
            for field in config[section]:
                field_row.add(field)
                tmp_row[field] = config[section][field]
            config_rows.append(tmp_row)
        csvwr = csv.DictWriter(csv_file, fieldnames=field_row)
        csvwr.writeheader()
        csvwr.writerows(config_rows)

