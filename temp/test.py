from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

def request_url(url):
    return urlopen(url)

def find_html_tag(soup):
    pass

def find_tourism():
    pass

def store_tourism():
    pass

if __name__ == "__main__":
    # 1. URL 요청
    # https://www.tripadvisor.co.kr/Attractions-g294197-Activities-Seoul.html
    # trip_adviser_url = "https://www.tripadvisor.co.kr/Attractions-g294196-Activities-South_Korea.html"
    trip_adviser_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-Seoul.html"

    # url에 html문서가 있음
    url = request_url(trip_adviser_url)

    # 2. HTML 문서 받고
    soup = bs(url, "lxml")

    # 전체 컨텐츠 리스트
    # all_tourism_list = (soup
    #                     .body
    #                     .find(name="div", attrs={"id": "PAGE"})
    #                     .find(name="div", attrs={"id": "MAINWRAP"})
    #                     .find(name="div", attrs={"id": "MAIN"})
    #                     .find(name="div", attrs={"id": "BODYCON"})
    #                     .find(name="div", attrs={"id": "ATTRACTIONS_NARROW"})
    #                     .find(name="div", attrs={"id": "AL_LIST_CONTAINER"})
    #                     .find(name="div", attrs={"id": "taplc_attraction_coverpage_attraction_0"})
    #                     .find(name="div")
    #                     .find_all(name="div", attrs={"class": "attractions_coverpage_widget coverpage_clarity"})
    #                     )

    # for temp_tourism_item in all_tourism_list:
    #     # 각 컨텐츠 리스트
    #     tourism_item_list = (temp_tourism_item
    #                          .find(name="div", attrs={"class": "prw_rup prw_shelves_shelf_widget"})
    #                          .find(name="div", attrs={"class": "shelf_item_container"})
    #                          .find_all(name="div", attrs={"class": "prw_rup prw_shelves_attraction_shelf_item_widget"})
    #                          )
    #
    #     for temp_item in tourism_item_list:
    #         # 각 컨텐츠 안에 항목(아이템)들
    #         tourism_item = (temp_item
    #                         .find(name="div", attrs={"class": "poi"})
    #                         .find(name="div", attrs={"class": "detail"})
    #                         .find(name="div", attrs={"class": "item name"})
    #                         .find(name="a").text
    #                         )
    #         print(tourism_item)
    #
    #     print("")
    i = 1
    for temp in soup.find_all(name="div", attrs={"class":"attractions_coverpage_widget coverpage_clarity"}):
        content_name = temp.find(name="a", attrs={"class":"ui_link title_text"}).text
        for temp1 in temp.find_all(name="div", attrs={"class":"item name"}):
            print(str(i) + " : " + content_name + " : " + temp1.find(name="a").text)
            i += 1