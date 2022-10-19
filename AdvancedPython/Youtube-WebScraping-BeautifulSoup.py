
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/playlist?list=PLzcys7whQ6eSJdSHJh-xdOLvWPP24J76x"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

# result = soup.find('div', {'id':'content'})
# result = result.find('ytd-page-manager', {'id':'page-manager'}).find('ytd-browse').find('ytd-two-column-browse-results-renderer').find('div', {'id':'primary'})
# result = result.find('ytd-section-list-renderer').find('div', {'id':'contents'}).find('ytd-item-section-renderer').find('div', {'id':'content'})
# mylist = result.find('ytd-playlist-video-list-renderer').find('div', {'id':'contents'}).find_all('ytd-playlist-video-renderer')
#/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]
# /ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[1]/div[2]/div[1]/div/h3/a
mylist = soup.div.div[1].div[2].div[3].a['title']

index = 1
for title in mylist:
    print(f"\n{index}. {title}")
    index+=1
