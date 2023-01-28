import re
import pandas as pd

headers = ['area_name', 'tot_vaccined', 'tot_vaccined_rate']
f = open("result.csv", "r")

f.readline()
items = []
while 1:
    item = []
    info = f.readline().split(',')
    if info is None or info[0] == '':
        break
    item.append(info[0])
    if info[1] == '':
        item.append(None)
    else:
        val = float(re.findall(r"\d+\.?\d*", info[1])[-1])
        if info[1].split(' ')[-1].replace('\n', '') == 'billion':
            val = val * 1000000000
            item.append(int(round(val, 0)))
        elif info[1].split(' ')[-1].replace('\n', '') == 'million':
            val = val * 1000000
            item.append(int(round(val, 0)))
        else:
            item.append(val)
    if info[2] == '\n':
        item.append(None)
    else:
        val = float(re.findall(r"\d+\.?\d*", info[2])[-1])
        item.append(val)
    items.append(item)

wf = pd.DataFrame(columns=headers, data=items)
af = wf.loc[(~wf['tot_vaccined'].isna()) & (wf['tot_vaccined_rate'].isna())]
bf = wf.loc[(wf['tot_vaccined'].isna()) & (~wf['tot_vaccined_rate'].isna())]
del af['tot_vaccined_rate']
del bf['tot_vaccined']
df = pd.merge(af, bf, how='inner', on='area_name')
df.to_csv("result-vaccined.csv", index=None)
