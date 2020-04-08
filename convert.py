import csv
import yaml


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
#
csv_file_name = 'gdpr_config_dtl.csv'
yaml_file_name = 'gdpr_config_dtl.yaml'
header = ["REL_CTGRY_TXT","TBL_NM","ATT_NM","UPDT_VAL_TXT","ACTIVE_FLG"]

class Config():
    def __init__(self):
        self.category = dict()
        self.conf = list()
        # {'GDPR12': [{'table':'CLM','columns':['col1','col2']},...]}
    def add_category(self, p_category):
        exist_flag = False
        for i in self.conf:
            exist_flag = True if p_category in i else False
        if not exist_flag:
            self.conf.append({p_category : list()})
        #print(self.conf)
    def get_category_list(self, p_category):
        for i in self.conf:
            if p_category in i:
                #print('p_category return:',i[p_category])
                return i[p_category]
    def upd_category_list(self, p_category, p_new_list):
        new_cat = list()
        for i in self.conf:
            if p_category in i:
                new_cat = p_new_list
            else:
                new_cat.append(list)
        i[p_category] = new_cat

    def upd_table(self, p_category, p_table, p_column):
        self.add_category(p_category)
        cat_list = self.get_category_list(p_category)
        new_cat_list = list()
        table_dict = dict()
        for t in cat_list:
            #print(t)
            if t['table'] == p_table:
                #print('update')
                #print(t)
                table_dict['table'] = t['table']
                table_dict['columns']=t['columns']
                table_dict['columns'].append(p_column)
                #print(table_dict)
                new_cat_list.append(table_dict)

            else:
                #print('add')
                new_cat_list.append(t)
        if not bool(table_dict):
            new_cat_list.append({'table' : p_table, 'columns':[p_column]})
            #print('new_cat_list',new_cat_list)
        self.upd_category_list(p_category,new_cat_list)

    def show_me (self):
        return self.conf

conf_list = list()
conf_dict = dict()
conf = Config()
with open (csv_file_name,'r+') as c:
    reader = csv.DictReader(c, delimiter=',', fieldnames=header)
    next(reader,None)
    for row in reader:
        #conf.upd_category(row["REL_CTGRY_TXT"])
        conf.upd_table(row["REL_CTGRY_TXT"], row["TBL_NM"], row["ATT_NM"])
#print(conf.show_me())
ydoc = yaml.dump(conf.show_me(),default_flow_style=False, sort_keys=False)
print(ydoc)
with open (yaml_file_name,'w') as y:
    y.write(ydoc)
