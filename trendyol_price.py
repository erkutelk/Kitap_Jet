import logging
from bs4 import BeautifulSoup
import requests
from time import sleep
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

class TrendyolFiyat:
    satici=1
    def __init__(self, url):
        self.list=[]
        try:
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
            })
            self.url = url
            response = self.session.get(self.url)
            sleep(2)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.content, 'html.parser')
            print('Giriş Yapıldı...')
        except Exception as e:
            logging.error(f'Giriş yapılırken bir hata meydana geldi: {e}')
            self.soup = None

    def yazi_al(self, kitap_name, price,satici_puani,bizim_fiyat):
        if self.soup:
            kitap = self.soup.select(kitap_name)
            fiyat_text = self.soup.select(price)
            satici_puanı=self.soup.select(satici_puani)
            bizim_satigimiz_fiyat=self.soup.select(bizim_fiyat)
            if not kitap:
                logging.warning('Satıcı bilgisi bulunamadı.')
                
            if not fiyat_text:
                logging.warning('Fiyat bilgisi bulunamadı.')
            for a, b,c,d in zip(kitap, fiyat_text,satici_puanı,bizim_satigimiz_fiyat):
                dicit={'Diger Satici':a.get_text(),
                       'Kitap Fiyatı':b.get_text().strip().replace(',','.'),
                       'Satıcı Puanı':c.get_text(),
                       'Bizim Sattığımız Fiyat':d.get_text()}
                
                self.list.append(dicit)
        else:
            logging.error('Sayfa içeriği alınamadı.')

    def yazdir(self):
        for a in self.list:
            diger_satici=a['Diger Satici']
            kitap_fiyat=a['Kitap Fiyatı']
            satici_puan=a['Satıcı Puanı']
            Bizim_Fiyat=a['Bizim Sattığımız Fiyat']
            print(f"{self.satici}-) Diğer Satıcı İsmi:> {diger_satici}\nKitap Fiyatı:> {kitap_fiyat}\nSatıcı puanı:> {satici_puan}\n--------------")
            self.satici+=1



    
    def bizimFiyat(self):
        a = self.soup.find('#product-detail-app > div > div.flex-container > div > div:nth-child(2) > div:nth-child(2) > div > div.product-detail-wrapper > div.pr-in-w > div > div > div.product-price-container > div > div > span')
        if a:
            for item in a:
                print('Bizim Satış Fiyatımız',item.get_text())  

    
