import pandas as pd
import yaml
#header=["REL_CTGRY_TXT","PRNT_TBL_NM","PRNT_COL_NM","CHLD_TBL_NM","CHLD_COL_NM","ACTIVE_FLG"]
header=["category","parentTable","parentColumn","childTable","childColumn","active"]

def get_nested_rec(key, grp):
    rec = dict()
    #al = dict()
    rec['category'] = key[0]
    rec['parentTable'] = key[1]
    rec['parentColumn'] = key[2]

    df_childs = grp[['childTable','childColumn']]
    #print(df_childs.to_dict('r'))
    rec['childs'] = df_childs.to_dict('r')
    #vals=list()
    #for r in grp
    #val['childTable']= grp['childTable']
    #val['childColumn']=grp['childColumn']
    #vals.append(df_childs.to_dict('r'))
    return rec


df = pd.read_csv('prnt_chld_rel.csv',header=0,names=header)
#print(df.head)
records=list()
for key, grp in df.groupby(["category","parentTable","parentColumn"]):
    rec = get_nested_rec(key, grp)
    #print(grp.filter(items=['childTable', 'childColumn']))
    #print(rec)
    records.append(rec)

print(yaml.dump(records))
#print(records)
