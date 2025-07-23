from bs4 import BeautifulSoup
import requests
import csv

list=[]

url="https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html?"

response=requests.get(url)
response.encoding = "utf-8"
soup=BeautifulSoup(response.text,"html.parser")

print(f"_________{soup.find("h1").text}__________")

print("\n------------------------------------------\n")
sayac=1
all_books_articles=soup.find_all("article", class_="product_pod")

for i in all_books_articles:
    name=i.find("h3").find("a")
    para=i.find("div",class_="product_price").find("p")
    stock=i.find("div",class_="product_price").find("p",class_="instock availability")
    link=i.find("div",class_="image_container").find("a")
    ready_link=link.get("href")
    x=f"https://books.toscrape.com/catalogue/category/books/science-fiction_16/{ready_link}"
    if stock and name and para:
        ready_para=para.text
        ready_name=name.text
        ready_stock=stock.text.strip()
        veriler={
            "İsim":ready_name,
            "Para":ready_para,
            "Stock":ready_stock,
            "Link":x
        }
        list.append(veriler)
    
    else:continue
    
    print(f"{sayac}-{ready_name} | Buy: {ready_para} | {ready_stock}")
    print(f"Link: https://books.toscrape.com/catalogue/category/books/science-fiction_16/{ready_link}")
    sayac+=1
    print()
    print()

dosya_adi = 'C:/Users/yakup/OneDrive/Desktop/projeler/proje4/kitap_verileri.csv'

alan_isimleri = ['İsim', 'Para', 'Stock', 'Link'] 

with open(dosya_adi, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=alan_isimleri)
    
    writer.writeheader() 
    writer.writerows(list)

print(f"\n___________________________________________\n")
print(f"Veriler başarıyla '{dosya_adi}' dosyasına kaydedildi.")
print(f"Dosya, Python kodunuzun bulunduğu klasörde yer almaktadır.")
