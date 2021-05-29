import pandas as pd
from pathlib import Path
import json
import csv

p = Path('/home/janekkttme/Документы/FindIt/webScraping/jsonFiles/prepdata_HM.json')

open('data_HM.csv', 'w').close()
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())
    
df = pd.json_normalize(data)

df.to_csv('data_HM.csv', index=False, encoding='utf-8')

p = Path('/home/janekkttme/Документы/FindIt/webScraping/jsonFiles/prepdata_ItemHM.json')

open('data_ItemHM.csv', 'w').close()
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())
    
df = pd.json_normalize(data)

df.to_csv('data_ItemHM.csv', index=False, encoding='utf-8')


# ADD
df = pd.read_csv('data_HM.csv')

description=[]
    
with open('/home/janekkttme/Документы/FindIt/webScraping/data_ItemHM.csv', 'r', encoding='utf-8') as d:
    reader = csv.reader(d)
    for row in reader:
        description.append(row[1])
description.pop(0)
 
df['description'] = description     
                
df.to_csv('data_HM.csv')
