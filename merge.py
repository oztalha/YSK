# coding: utf-8

import xlrd # http://www.simplistix.co.uk/presentations/python-excel.pdf
import csv
from glob import glob
from collections import Counter
import StringIO

# TR sehir kodlari
tr = dict()
with open('plaka.tsv') as plakalar:
    for plaka in plakalar:
        il, kod = plaka.split('\t')
        tr[il.decode('utf8').strip()] = kod.strip()

# GSKD datasi: Tuik Nisan 2014 raporu, Ek 5 (sayfa 57)
# http://www.tuik.gov.tr/jsp/duyuru/upload/yayinrapor/GSKD_Bolgesel_2004-2011.pdf
gskd = []
with open('GSKD.csv', 'rb') as f:
    reader = csv.reader(f)
    for utf8_row in reader:
        unicode_row = [x.decode('utf8') for x in utf8_row]
        gskd.append(unicode_row)

# GSKD datasinin temizlenmesi ve ilk analizi
partiler = Counter()
#mahalleler = Counter()
for i in range(2,len(gskd)):
    iller = [il.strip() for il in gskd[i][1].split(', ')]
    for il in iller:
        ilceler = glob('sspsYerel-'+tr[il]+'-*')
        for ilce_xls in ilceler:
            ilce = open_workbook(ilce_xls,on_demand=True).sheets()[0]
            try:
                partiler.update(ilce.row_values(1)[13:])
                #if mahalleler.has_key('-'.join(ilce.row_values(2)[:5])):
                #    os.remove(ilce_xls)
                #    print ilce_xls
                #mahalleler.update(['-'.join(ilce.row_values(2)[:5])])
            except IndexError:
                print "IndexError",ilce_xls

# GSKD'deki her bolge icin uc buyuk parti ve 'diger' oylari
fields = [u'IL_ID', u'ILCE_ID', u'MUHTARLIK_ID', u'\u0130l', u'Se\xe7im \xc7evresi', u'Mahalle / K\xf6y',
u'Sand\u0131k No', u'Sand\u0131k Se\xe7men Listesinde Yaz\u0131l\u0131 Se\xe7menlerin Say\u0131s\u0131',
u'Oy Kullanan Se\xe7men Say\u0131s\u0131', u'\u0130tiraz Edilmeksizin Ge\xe7erli Say\u0131lan Oy Pusulalar\u0131n\u0131n Say\u0131s\u0131',
u'\u0130tiraz \xdczerine Ge\xe7erli Say\u0131lan veya Hesaba Kat\u0131lan Oy Pusulalar\u0131n\u0131n Say\u0131s\u0131',
u'Ge\xe7erli Oy Pusulalar\u0131n\u0131n Toplam\u0131', u'Ge\xe7ersiz Say\u0131lan veya Hesaba Kat\u0131lmayan Oy Pusulalar\u0131n\u0131n Toplam\u0131']
# partilerin/bagimsiz adaylarin yayginlik sirasinca
fields.extend(zip(*partiler.most_common(10))[0])
fields.append(u'Diger')
sandiklar = []
for i in range(2,len(gskd)):
    iller = [il.strip() for il in gskd[i][1].split(', ')]
    for il in iller:
        ilceler = glob('sspsYerel-'+tr[il]+'-*')
        for ilce_xls in ilceler:
            ilce = open_workbook(ilce_xls,on_demand=True).sheets()[0]
            ilce_fields = ilce.row_values(1)
            for row in range(2,ilce.nrows):
                orgsandik = ilce.row_values(row)
                sandik = orgsandik[:13]
                sandik.extend([0 for x in range(13,len(fields))])
                for col in range(13,len(ilce_fields)):
                    if ilce_fields[col] in fields:
                        sandik[fields.index(ilce_fields[col])] = int(orgsandik[col])
                    else:
                        sandik[len(fields)-1] += int(orgsandik[col])
                sandiklar.append(sandik)

#Excel icin tab separated utf-16
with open('yerel2014.csv','wb') as fout:
    writer = UnicodeWriter(fout,quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fields)
    for line in sandiklar:
        writer.writerow(line)

#Sair programlar icin utf-8 ve comma separated
with open('tum_sandiklar.csv','wb') as fout:
    writer = UnicodeWriter(fout,delimiter=',',encoding="utf-8",quoting=csv.QUOTE_ALL)
    writer.writerow(fields)
    for line in sandiklar:
        writer.writerow(line)


class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel_tab, encoding="utf-16", **kwds):
        # Redirect output to a queue
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f

        # Force BOM
        if encoding=="utf-16":
            import codecs
            f.write(codecs.BOM_UTF16)

        self.encoding = encoding

    def writerow(self, row):
        # Modified from original: now using unicode(s) to deal with e.g. ints
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = data.encode(self.encoding)

        # strip BOM
        if self.encoding == "utf-16":
            data = data[2:]

        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
