from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# 코딩 컨벤션
# 동사 원청 + 명사

def request_url(url):
   return urlopen(url)

def find_html_tag():
   pass

def find_tourism():
   pass

def store_tourism():
   pass



if __name__ == "__main__":
   # 1. URL 요청

   trip_adviser_url = "https://www.tripadvisor.co.kr/Restaurants-g294197-Seoul.html"

   # url에 html문서가 있음
   url = request_url(trip_adviser_url)

   # 2. HTML 문서 받고
   print(url)
   soup = bs(url,"lxml")

   # 3. 태그 찾기
   all_tourism_list = (soup
                       .body
                       .find(name="div",attrs={"id":"PAGE", "class":"filterSearch redesign_2015 non_hotels_like desktop scopedSearch"})
                       .find(name="div",attrs={"class":" hotels_lf_redesign ui_container is-mobile responsive_body"})
                       .find(name="div",attrs={"class": "Restaurants prodp13n_jfy_overflow_visible "})
                       .find(name="div",attrs={"id":"BODYCON", "class": "col easyClear poolC adjust_padding new_meta_chevron_v2"})
                       .find(name="div",attrs={"class": "eateryOverviewContent"})
                       .find(name="div",attrs={"class": "ui_columns is-partitioned is-mobile"})
                       .find(name="div",attrs={"class": "ui_column is-9"})
                       .find(name="div",attrs={"class": "coverpage", "id":"COVERPAGE_BOX"})
                       .find(name="div",attrs={"class": "ppr_rup ppr_priv_restaurants_coverpage_content", "id":"taplc_restaurants_coverpage_content_0"})
                       .find(name="div",attrs={"class": "coverpage_widget"})
                       .find(name="div",attrs={"class": "prw_rup prw_shelves_shelf_widget"})
                       .find(name="div",attrs={"class": "shelf_container restaurants_by_filter shelf_row_2"})
                       .find(name="div",attrs={"class": "shelf_item_container "})
                       .find(name="div",attrs={"class": "prw_rup prw_shelves_restaurant_shelf_item_widget"})
                       .find(name="div",attrs={"class": "prw_rup prw_shelves_restaurant_shelf_item_widget"})
                       .find(name="div",attrs={"class": "prw_rup prw_shelves_restaurant_shelf_item_widget"})
                       .find(name="div",attrs={"class": "prw_rup prw_shelves_restaurant_shelf_item_widget"})

                       )
   print(all_tourism_list)
   # 4. 어떤 관광지인지 받기
   # 5. HOT 관광지 데이터베이스에 저장