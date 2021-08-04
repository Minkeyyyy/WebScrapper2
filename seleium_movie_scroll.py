import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument("window-size=1920x1080")
# headless chrome이면 웹사이트에서 정보를 안줄 수 있다.
# 종종 user agent를 바꿔줄 필요가 있다.
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")

url = "https://play.google.com/store/movies/top"
interval = 2
browser = webdriver.Chrome(options=options)
browser.maximize_window()

browser.get(url)

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤 가장 아래 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 끝")
browser.get_screenshot_as_file("google_movie.png")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}

# res = requests.get(browser.page_source, headers=headers)
# res.raise_for_status()
soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
# print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    # else:
    #     print("할인 되지 않는 영화")

    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 : {original_price}")
    print(f"할인 후 : {price}")
    print(f"링크 : https://play.google.com{link}")
    print("=="*50)

browser.quit()
