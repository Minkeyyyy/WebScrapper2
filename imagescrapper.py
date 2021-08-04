import requests
from bs4 import BeautifulSoup
import re


url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EA%B0%9C%EB%B4%89%EC%98%88%EC%A0%95%EC%98%81%ED%99%94"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
images = soup.find("div", attrs={"class", "card_area _panel"}).find_all(
    "a", attrs={"class", "img_box"})

for image in images:
    image_url = image.find("img")
    if image_url:
        print(image_url["src"]) 
