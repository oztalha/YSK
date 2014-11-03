YSK
===

YSK (Yuksek Secim Kurulu) 2014 Yerel secim sonuclarini indiren, duzenleyen, analiz edn script'ler ve de sonuc dosyalari.

Scripts to scrape ballot-box level official vote counts, to clean/reformat/combine resulting files, and to recalculate GPD weighted votes for Turkey's 2014 local election.
Codes are commented, short deescriptions of the files are as follows:

- **scrape.py**: Scrapes Turkish local elections, 2014 results from ysk.gov.tr (official election institute).
- **merge.py**: Cleans and reformats the collected data and combine them into a single CSV file.
- **plaka.tsv**: A helper file to map the cities to their traffic codes.                                                                                                
- **plaka.tsv**: A helper file to map the cities to their traffic codes.
- **GSKD.csv**: GDP per capita table for 26 regions (extracted from [TUIK April 2014 report](http://www.tuik.gov.tr/jsp/duyuru/upload/yayinrapor/GSKD_Bolgesel_2004-2011.pdf)).
- **kd_oylar.py**: Recalculates parties' vote shares weighted by 26 regions' GDP.
- **kd_oylar.csv**: GDP per region weighted votes resulting file.
- **yerel2014.csv**: Official ballot-box level results of the top ten parties' in Turkish local elections, 2014.
- **Yerel-GSKD-TR.png (Turkish Title)** and **GDP-Weighted-TR-2014-local.png (English Title)**: Pie chart of recalculated vote shares of parties if GDP voted not people. Replicated what [the Guardian](http://www.economist.com/blogs/graphicdetail/2015/10/daily-chart-18) did for Brazil.
