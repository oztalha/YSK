YSK
===

*YSK (Yuksek Secim Kurulu) 2014 Yerel secim sonuclarini indiren, duzenleyen, analiz edn script'ler ve de sonuc dosyalari.*

This project consists of scripts to scrape ballot-box level official vote counts from [YSK](https://sonuc.ysk.gov.tr/), to clean/reformat/combine resulting files, and to recalculate GPD weighted votes for Turkey's 2014 local election. Codes are commented, short deescriptions of the files are as follows:

- **scrape.py**: Scrapes Turkish local elections, 2014 results from ysk.gov.tr (official election institute).
- **merge.py**: Cleans and reformats the collected data and combines them into a single CSV file.
- **plaka.tsv**: A helper file to map the cities to their traffic codes.                                                                                                
- **GSKD.csv**: RGVA per capita table for 26 regions (extracted from [TUIK April 2014 report](http://www.tuik.gov.tr/jsp/duyuru/upload/yayinrapor/GSKD_Bolgesel_2004-2011.pdf)).
- **weighted_votes.py**: Recalculates parties' vote shares weighted by 26 regions' RGVA (per head).
- **kd_oylar.csv**: RGVA per head weighted votes resulting file (output of the weighted_votes.py script).
- **yerel2014.csv**: Official ballot-box level results of the top ten parties in Turkish local elections, 2014 (output of the merge.py script).
- **TR-2014-RGVA.png** (output of grafik_analiz.xlsx): Pie charts of the [official election results](http://www.ysk.gov.tr/cs/groups/public/documents/document/ndq0/mda0/~edisp/yskpwcn1_4444004537.pdf) and recalculated RGVA (per head) weighted vote shares of parties. Similar to what [the Economist](http://www.economist.com/blogs/graphicdetail/2014/10/daily-chart-18) did for Brazil.
- **grafik_analiz.xlsx**: Transforms vote counts to shares and generates the pie charts.
