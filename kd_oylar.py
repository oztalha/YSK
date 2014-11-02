# coding: utf-8
import csv
import pandas as pd
import numpy as np

# TR sehir kodlari
tr = dict()
with open('plaka.tsv') as plakalar:
    for plaka in plakalar:
        il, kod = plaka.split('\t')
        tr[il.decode('utf8').strip()] = kod.strip()

gskd = []
with open('GSKD.csv', 'rb') as f:
    reader = csv.reader(f)
    for utf8_row in reader:
        unicode_row = [x.decode('utf8') for x in utf8_row]
        gskd.append(unicode_row)

df = pd.read_csv('yerel2014.csv',encoding='utf-16',delimiter='\t')

kd_oylar = np.zeros(11)
for i in range(2,len(gskd)):
    iller = [il.strip() for il in gskd[i][1].split(', ')]
    oylar = np.zeros(11)
    for il in iller:
        print il
        iloy = get_votes(il,df)
        oylar = np.add(oylar, iloy)
    #kd = int(float(gskd[i][16])*1000)
    bolge_kd_oylar = oylar*float(gskd[i][16])
    kd_oylar = np.vstack((kd_oylar,bolge_kd_oylar))

#ilk satir manuel olarak degistirildi
np.savetxt('kd_oylar.csv',kd_oylar,delimiter=',',fmt="%d")

def get_votes(il,df):    
    oylar = []
    for parti in df.columns[13:]:
        oylar.append(df[df.IL_ID == int(tr[il])][parti].sum())
    return np.asarray(oylar)