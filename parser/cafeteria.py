from bs4 import BeautifulSoup
import requests, time

def students_hall():
    url = "http://m.sejong.ac.kr/front/cafeteria.do"
    result = requests.post(url, data={"type1":"0"})
    content = BeautifulSoup(result.text, 'html.parser')

    print("*학생회관")
    menu = content.find("tbody").get_text(' ').split('\n')

    buf = []
    for menu_list in menu:
        if menu_list:
            buf.append(menu_list)
    menu = '\n'.join(buf)
    return menu

def woojung():
    url = "http://m.sejong.ac.kr/front/cafeteria.do"
    result = requests.post(url, data={"type1":"2"})
    content = BeautifulSoup(result.text, 'html.parser')

    days = ['월', '화', '수', '목', '금', '토', '일']
    today = time.localtime().tm_wday

    buf = []
    for i in range(1,6):
        menu = content.find("div", {'class':'h2 seq-0' + str(i)}).find("div", {'class':'table'}).get_text()
        menu = menu.replace('\r', '').replace('\t', '').split('\n')#.replace('\n', '')
        for menu_list in menu:
            if menu_list != "식당메뉴":
                if menu_list:
                    buf.append(menu_list)
    return "\n".join(buf)

def gunja():
    url = "http://m.sejong.ac.kr/front/cafeteria.do"
    result = requests.post(url, data={"type1":"3"})
    content = BeautifulSoup(result.text, 'html.parser')

    days = ['월', '화', '수', '목', '금', '토', '일']
    today = days[time.localtime().tm_wday]
    tomorrow = days[(time.localtime().tm_wday+1)%7]

    menu = content.find("div", {'class':'h2 seq-01'}).get_text().replace('\r', '').replace('\t', '').split('\n')
    #menu = menu.replace('\r', '').replace('\t', '').split('\n')#.replace('\n', ' ')
    
    buf = []
    for menu_list in menu:
        if menu_list:
            buf.append(menu_list)

    today = [s for s in buf if today + '(' in s][0]
    tomorrow = [s for s in buf if tomorrow + '(' in s][0]
    menu_today = '\n'.join(buf[buf.index(today):buf.index(tomorrow)]).replace("석식","\n석식")

    return menu_today