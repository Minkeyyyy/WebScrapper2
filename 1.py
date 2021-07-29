import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#cartoons = soup.find_all("td", attrs={"class": "title"})
# 제목과 링크 가져오기.
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "http://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

cartoons = soup.find_all("div", attrs={"class": "rating_type"})
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate)

print(total_rates / len(cartoons))
