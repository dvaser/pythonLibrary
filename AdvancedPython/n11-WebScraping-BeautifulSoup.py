
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.findAll("li", {"class":"column"})

for li in list:
    name = li.find("div", {"class":"columnContent"}).find("div", {"class":"pro"}).find("a").find("h3").text.strip()
    price = li.input['value']
    print(f"\nName: {name}\nPrice: {price}")