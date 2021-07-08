import requests
from bs4 import BeautifulSoup as bs
import random
import time


# --------------- 게임 시작 화면 ------------------- #

subway_num = 0

def subway_intro():
    print("♪ ♬  지하철~! 지하철 지하철~! 지하철       ♪ ♬")
    print("♪ ♬  몇호선~? 몇호선 몇호선 몇호선 몇호선?  ♪ ♬")
    while True:
        try:
            subway_num = input("1~9 숫자를 입력해주세요 : ")
            int(subway_num)
        except ValueError:
            print("1~9 사이의 숫자를 입력해주세요!")
        else:
            if int(subway_num) not in [i for i in range(1,10)]:
                print("1~9 사이의 숫자를 입력해주세요!")
            else:
                break

    
    return subway_num

def subway_main_game(subway_num, names, player):
    start_number = names.index(player)
    now = start_number - 1 
    length = len(names)
    stations = make_line_list(subway_num)
    already = []
    answer = 1
    
    while answer == 1:
        now += 1
        now = now % len(names)
        if now == 0:
            print("{}님의 차례입니다!".format(names[now]))
            input_sub_station = input("지하철 역 명을 입력하세요('역' 제외) :  ")
            if input_sub_station not in stations:
                answer = 0
                print("이런, {}호선엔 없는 역이예요 😢".format(subway_num) )
            elif input_sub_station in already:
                answer = 0
                print("이런, 이미 말한 역이예요 😢")
            elif input_sub_station in stations:
                print(" 다음 차례 !")
                already.append(input_sub_station)
            
        elif now != 0:
            prob = random.choices(range(0, 2), weights=[1,2])[0]
            time.sleep(0.2)
            if prob == 0:
                # 틀려야함
                wrong = make_wrong_station(subway_num)
                print("{} 님이 입력한 지하철 역: {}".format(names[now],wrong))
                if wrong not in stations:
                    answer = 0
                    print("이런, {}호선엔 없는 역이예요 😢".format(subway_num) )
                elif wrong in already:
                    answer = 0
                    print("이런, 이미 말한 역이예요 😢")
                elif wrong in stations:
                    print(" 다음 차례 !")
                    already.append(wrong)

            else:
                # 맞아야함
                computer_say = stations[random.randint(0, len(stations))]
                print("{} 님이 입력한 지하철 역: {}".format(names[now], computer_say))
                if computer_say in already:
                    answer = 0
                    print("이런, 이미 말한 역이예요 😢")
                else:
                    print(" 다음 차례 !")
                    already.append(computer_say)
        time.sleep(1)
    print("{} 님이 졌습니다.".format(names[now]))


def full_subway_game(names, player):
    subway_num = subway_intro()
    subway_main_game(subway_num, names, player)

def make_line_list(subway_num):
    key = "455959635a676b7235354856525852"
    line = "0"+subway_num + "호선"
    url_line = f"http://openapi.seoul.go.kr:8088/{key}/xml/SearchSTNBySubwayLineInfo/1/100/ / /{line}"
    res = requests.get(url_line).text
    soup = bs(res, "html.parser")

    return [item.text for item in soup.select("station_nm")]

def make_wrong_station(subway_num):
    key = "455959635a676b7235354856525852"
    line = str(int(subway_num) + random.randint(1,8)%9)
    if line == 0:
        line = "9"
    line = "0"+ line + "호선"
    url_line = f"http://openapi.seoul.go.kr:8088/{key}/xml/SearchSTNBySubwayLineInfo/1/100/ / /{line}"
    res = requests.get(url_line).text
    soup = bs(res, "html.parser")

    return [item.text for item in soup.select("station_nm")][random.randint(0,10)]
