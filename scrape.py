# coding: utf-8
from splinter import Browser
import time

# NOT-1: tarayici olarak chrome'u kullanmak isterseniz
# driver'i indirip path'inize eklemeniz gerekiyor; linki:
# http://chromedriver.storage.googleapis.com/index.html
# eger firefox kullanmak isterseniz tarayicinin yuklu olmasi yeterli
# yalniz, bir defaliga mahsus bir ayar yapmaniz gerekiyor (bkz. NOT-2)

browser = Browser('firefox')
#Secim sonuclari sayfasi
browser.visit("https://sonuc.ysk.gov.tr/module/GirisEkrani.jsf")
#Browser tavsiye ekrani
browser.find_by_name('closeMessageButton').click()
#Yerel secimler 2014
browser.choose('j_id111:secimSorgulamaForm:j_id114:secimSecmeTable:1:secimId','true')
browser.find_by_name('j_id111:secimSorgulamaForm:j_id141').first.click()

# NOT-2: Eger tarayici olarak firefox'u secti isteniz tam bu asamada
# herhangi bir ilcenin datasini manuel olarak indirmeye calisin
# karsiniza cikan pencerede her zaman kaydet kutucugunu seciniz !

for il in range(0,82):
    browser.select('j_id47:j_id48:j_id88:cmbIl',str(il))
    time.sleep(2) # ilcelerin dolmasini bekle
    ilce_sayisi = len(browser.find_by_id("j_id47:j_id48:j_id100:cmbSecimCevresi").first.find_by_tag('option'))-1
    for i in range(0,ilce_sayisi):
        i = i + 1 #ilce indexi [1,ilce_sayisi] araliginda
        ilceler = browser.find_by_id("j_id47:j_id48:j_id100:cmbSecimCevresi").first.find_by_tag('option')
        browser.select('j_id47:j_id48:j_id100:cmbSecimCevresi',ilceler[i].value)
        time.sleep(2) #lutfen bekleyinizi bekle :S
        browser.find_by_name('j_id47:j_id48:j_id125').first.click()
        time.sleep(3) #sorgulamasini bekle 3 sn
        browser.find_by_id("j_id47:tabloBilgileriPanel:j_id367").first.click()
        time.sleep(2) #kabul ediyorum mesajini bekle 2 sn
        browser.find_by_id("j_id426:j_id427:j_id433").first.click()
        time.sleep(5) #excel dosyasini indirmesini bekle 5 sn
