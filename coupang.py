import requests
from bs4 import BeautifulSoup
import re


def extract_items(items):
    # 페이지의 items에서 정보득들 추출
    for item in items:
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            #print("==광고 상품은 제외합니다==")
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()
        if "Apple" in name:
            #print("==Apple 제품은 제외합니다.==")
            continue

        price = item.find("strong", attrs={"class": "price-value"}).get_text()
        rate = item.find("em", attrs={"class": "rating"})
        if not rate:
            #print("==평점이 없습니다.==")
            continue
        else:
            rate = rate.get_text()
        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"}).get_text()
        if not rate_cnt:
            # print("==평점 명수가 없습니다.==")
            continue
        else:
            rate_cnt = rate_cnt[1:-1]

        link = item.find("a")["href"]

        if int(rate_cnt) >= 100 and float(rate) >= 4.5:
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}")
            print(f"리뷰수: {rate_cnt}")
            print("바로가기 : {}".format("http://www.coupang.com" + link))
            print("----"*10)


for i in range(1, 6):
    print("///////////현재 페이지", i)
    url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&page={}".format(
        i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class": "name"}).get_text())
    extract_items(items)
