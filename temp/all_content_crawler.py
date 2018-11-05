from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

"""
URL 요청 함수
"""
def request_url(url):
    return urlopen(url)


"""
전체 컨텐츠 
=> 각 컨텐츠의 리스트 
=> 각 컨텐츠의 항목정보를 리스트 형태로 만들어주는 함수
"""
def find_all_content_item(soup):
    # 전체 컨텐츠 리스트
    all_tourism_list = (soup
                        .body
                        .find(name="div", attrs={"id": "PAGE"})
                        .find(name="div", attrs={"id": "MAINWRAP"})
                        .find(name="div", attrs={"id": "MAIN"})
                        .find(name="div", attrs={"id": "BODYCON"})
                        .find(name="div", attrs={"id": "ATTRACTIONS_NARROW"})
                        .find(name="div", attrs={"id": "AL_LIST_CONTAINER"})
                        .find(name="div", attrs={"id": "taplc_attraction_coverpage_attraction_0"})
                        .find(name="div")
                        .find_all(name="div", attrs={"class": "attractions_coverpage_widget coverpage_clarity"})
                        )

    for temp_tourism_item in all_tourism_list:
        # 각 컨텐츠 리스트
        tourism_item_list = (temp_tourism_item
                             .find(name="div", attrs={"class": "prw_rup prw_shelves_shelf_widget"})
                             .find(name="div", attrs={"class": "shelf_item_container"})
                             .find_all(name="div", attrs={"class": "prw_rup prw_shelves_attraction_shelf_item_widget"})
                             )

        for temp_item in tourism_item_list:
            # 각 컨텐츠 안에 항목(아이템)들
            tourism_item = (temp_item
                            .find(name="div", attrs={"class": "poi"})
                            .find(name="div", attrs={"class": "detail"})
                            .find(name="div", attrs={"class": "item name"})
                            .find(name="a").text
                            )
            print(tourism_item)
        print("")


if __name__ == "__main__":
    # 관광지 변수


    # URL 세팅
    trip_adviser_url = "https://www.tripadvisor.co.kr/Attractions-g294196-Activities-South_Korea.html"

    # URL 요청
    url = request_url(trip_adviser_url)

    # URL을 beatifulsoup 객체로 바꿈
    soup = bs(url, "lxml")

    # 관광지 정보 파싱
