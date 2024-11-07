import json


with open('kitaplar.json', 'r', encoding='utf-8') as dosya:
    veriler = json.load(dosya)
    
    for a in veriler:
        if 'link' in a:
            print(a['link'])

