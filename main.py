from trendyol_price import TrendyolFiyat
import json
import time
with open('kitaplar.json', 'r', encoding='utf-8') as dosya:
    veriler = json.load(dosya)

    for a in veriler:
            print(a['link'])
            value = TrendyolFiyat(a['link'])
            time.sleep(2)
            value.yazi_al(  kitap_name='.seller-name-text',
                                price='.mc-ct-rght .pr-bx-w .pr-bx-nm .prc-dsc',
                                satici_puani='#product-detail-app > div > div.pr-omc > div.omc-cntr > div > div.mc-ct-lft > div.pr-mb > div > div.sl-pn',
                                bizim_fiyat='.pr-bx-nm>span')
            value.yazdir()
            value.bizimFiyat()
            
