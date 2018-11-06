from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from tourism_database import tourism_database
import threading

class tourism:
    def __init__(self, trend, name, address, content_type):
        self.trend = trend
        self.name = name
        self.address = address
        self.type = content_type

    def __str__(self):
        return "[" + self.trend + ", " + self.name + ", " + self.address + ", " + self.type + "]"

def crawling_content(url):
    end_point = "https://www.tripadvisor.co.kr" + str(url)
    content_url = urlopen(end_point)
    content_soup = bs(content_url, "lxml")

    content_type_soup = content_soup.find(name="div", attrs={"class":"detail"})
    content_type_list = content_type_soup.find_all(name="a")
    content_type = ""

    for temp_type in content_type_list:
        if(temp_type.text == "더 보기"):
            pass
        else:
            content_type = content_type + temp_type.text + ", "
    content_type = content_type[:-2]

    address_soup = content_soup.find(name="span", attrs={"class":"detail"})
    address_temp1 = address_soup.find(name="span", attrs={"class":"locality"})
    address_temp2 = address_soup.find(name="span", attrs={"class":"street-address"})

    if address_temp1 != None:
        total_address = address_temp1.text

    if address_temp2 != None:
        total_address = " " + address_temp2.text

    # print(content_type + " : " + total_address.strip())

    return content_type, total_address.strip()


def crawling_tripadviser():
    trip_adviser_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-Seoul.html"
    tourism_list = list()
    url = urlopen(trip_adviser_url)
    soup = bs(url, "lxml")

    for temp in soup.find_all(name="div", attrs={"class":"attractions_coverpage_widget coverpage_clarity"}):
        trend_name = temp.find(name="a", attrs={"class":"ui_link title_text"}).text

        for temp1 in temp.find_all(name="div", attrs={"class":"item name"}):
            name = temp1.find(name="a").text
            url = temp1.find(name="a")['href']
            content_type, address = crawling_content(url)
            tourism_item = tourism(trend_name, name, address, content_type)
            tourism_list.append(tourism_item)

    tb = tourism_database()
    tb.add_tourism_detail_list(tourism_list)
    return

if __name__ == "__main__":
    crawling_tripadviser()