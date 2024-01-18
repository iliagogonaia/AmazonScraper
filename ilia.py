from bs4 import BeautifulSoup
import requests
import csv

column_name = ['Name','Price', 'Rating']
csvfile = open('movie_data.csv', 'w', newline='', encoding='utf-8') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

url = "https://www.amazon.in/s?k=playstation+5&crid=1Q0U492M99R92&sprefix=playstation+%2Caps%2C240&ref=nb_sb_noss_2"
url2 = "https://www.amazon.in/s?k=playstation+5&page=2&qid=1704896211&ref=sr_pg_2"
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

}
webpage = requests.get(url,headers = HEADERS)
soup = BeautifulSoup(webpage.text,"html.parser")
psfives = soup.find_all("div",class_="puisg-col-inner")
scraped_psfives = []
for psfive in psfives:
    try:
        name_element = psfive.find("span", class_="a-size-medium a-color-base a-text-normal")
        if name_element:
            name = name_element.get_text().strip()
            scraped_psfives.append(name)
    except AttributeError as e:
        print(F"error procesing element: {e}") 

scraped_prices = []
for prices in psfives:
    try:
        price_element = prices.find("span",class_="a-price-whole")
        if price_element:
            price = price_element.get_text().strip()
            scraped_prices.append(price)
    except AttributeError as e:
        print(f"error procesing element: {e}")
scraped_rating = []
for ratings in psfives:
    try:
        rating_element = ratings.find("i",class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom")
        if rating_element:
            rating = rating_element.get_text().strip()
            scraped_rating.append(rating)
    except AttributeError as e:
        print(f"error procesing element: {e}")



for name, price, rating in zip(scraped_psfives, scraped_prices, scraped_rating):
    print(f"Name: {name}\nPrice: {price}\nRating: {rating}\n")
    csvwriter.writerow([name, price, rating])


webpage2 = requests.get(url2,headers = HEADERS)
soup2 = BeautifulSoup(webpage2.text,"html.parser")
psfives2 = soup2.find_all("div",class_="puisg-col-inner")
scraped_psfives2 = []
for psfive in psfives2:
    try:
        name_element2 = psfive.find("span",class_="a-size-medium a-color-base a-text-normal")
        if name_element2:
            name = name_element2.get_text().strip()
            scraped_psfives2.append(name)
    except AttributeError as e:
        print(f"error procesing element: {e}")
scraped_prices2 = []
for prices in psfives2:
    try:
        price_element2 = prices.find("span",class_="a-price-whole")
        if price_element2:
            price2 = price_element2.get_text().strip()
            scraped_prices2.append(price2)
    except AttributeError as e:
        print(f"error procesing element: {e}")
scraped_ratings2 = []
for ratings in psfives2:
    try:
        rating_element = ratings.find("i",class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom")
        if rating_element:
            rating = rating_element.get_text().strip()
            scraped_ratings2.append(rating)
    except AttributeError as e:
        print(f"error procesing element: {e}")

for name, price, rating in zip(scraped_psfives2, scraped_prices2, scraped_ratings2):
     print(f"Name: {name}\nPrice: {price}\nRating: {rating}\n")
     csvwriter.writerow([name, price, rating])
csvfile.close()






    




