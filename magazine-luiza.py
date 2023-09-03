# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup

search = input('qual produto deseja buscar: ')
page = input('qual página deseja buscar: ')
url = 'https://www.magazineluiza.com.br/busca/' + search + '?page=' + page

response = requests.get(url)
site = BeautifulSoup(response.content, 'html.parser')
products = site.find_all('div', attrs={'class': 'sc-AHTeh'})
products_data = []

for product in products:
    title = product.find('h2', {'class', 'sc-ijtseF'})
    price = product.find('p', {'class', 'eCPtRw'})
    
    if product.find('p', {'class', 'efxPhd'}) != None:
        old_price = product.find('p', {'class', 'efxPhd'})
    else:
        continue
    
    old_price = old_price.text.replace("R$", "")
    price = price.text.replace("R$", "")
    
    try:
        old_price = float(old_price.replace(".", "").replace(",", ".")) if len(old_price) > 7 else float(old_price.replace(",", "."))
        price = float(price.replace(".", "").replace(",", ".")) if len(price) > 7 else float(price.replace(",", "."))
        percent_change = float(format((price - old_price) / old_price, '.2f'))
    except:
        continue
    products_data.append({
        'name': title.text,
        'current_price': price,
        'old_price': old_price,
        'percent_chage': percent_change
    })
print(products_data)
    