import csv
import yaml
from collections import OrderedDict

csv_file_name = 'prnt_chld_rel.csv'
yaml_file_name = 'prnt_chld_rel.yaml'
header=["REL_CTGRY_TXT","PRNT_TBL_NM","PRNT_COL_NM","CHLD_TBL_NM","CHLD_COL_NM","ACTIVE_FLG"]
#header=["category","parentTable","parentColumn","childTable","childColumn","active"]
#{'g12': {'child': {'column': 'childcolumn', 'table': 'childtable'}, 'parent': {'column': 'clm_bus_id', 'table': 'CLM'}}}
conf_list = list()
with open (csv_file_name,'r+') as c:
    reader = csv.DictReader(c, delimiter=',', fieldnames=header)
    next(reader,None)
    for row in reader:
        conf_rec = dict()
        conf_rec={row["REL_CTGRY_TXT"] :
                    {'parent' :
                       {'table'  : row["PRNT_TBL_NM"],
                        'column' : row["PRNT_COL_NM"]
                       },
                     'child'  :
                        {'table'  : row["CHLD_TBL_NM"],
                         'column' : row["CHLD_COL_NM"]
                        },
                     'active' : 'Y' if row["ACTIVE_FLG"] == '1' else 'N'
                    }
                 }
        #print(conf_rec)
        conf_list.append(conf_rec)

ydoc = yaml.dump(conf_list,default_flow_style=False, sort_keys=False)
print(ydoc)
with open (yaml_file_name,'w') as y:
    y.write(ydoc)
