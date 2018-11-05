from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from tourism_database import tourism_database
import threading

def crawling_tripadviser():
    trip_adviser_url = "https://www.tripadvisor.co.kr/Attractions-g294197-Activities-Seoul.html"
    tourism_list = list()
    url = urlopen(trip_adviser_url)
    soup = bs(url, "lxml")

    i = 1
    for temp in soup.find_all(name="div", attrs={"class":"attractions_coverpage_widget coverpage_clarity"}):
        tourism_dict = dict()
        temp_list = list()

        content_name = temp.find(name="a", attrs={"class":"ui_link title_text"}).text
        tourism_dict['content_name'] = content_name

        for temp1 in temp.find_all(name="div", attrs={"class":"item name"}):
            # print(str(i) + " : " + content_name + " : " + temp1.find(name="a").text)
            temp_list.append(temp1.find(name="a").text)
            i += 1

        tourism_dict['content'] = temp_list
        tourism_list.append(tourism_dict)

    print(tourism_list)
    tb = tourism_database()
    tb.delete_tourism_list()
    tb.add_tourism_list(tourism_list)
    tb.close()

    threading.Timer(3600, crawling_tripadviser).start()


"""
MAIN
"""
if __name__ == "__main__":
    crawling_tripadviser()