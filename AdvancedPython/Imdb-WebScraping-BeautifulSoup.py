
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {'class':'lister-list'}).findAll("tr")

index = 1
for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    date = tr.find("td", {"class":"titleColumn"}).find("span").text
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"\n{index}. {title} {date}\nRating: {rating}")
    index+=1

