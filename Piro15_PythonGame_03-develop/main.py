from soupsieve import select_one
import subway
import random
import up_down
import Game_of_Death

player_num = 0
names = []
global computer 
computer = ["현주","송경","건웅","진혁"]
global max_alcohol 
max_alcohol= []

def game_setting(names, max_alcohol):
    print()
    print("=======================================================")
    print()
    player = input("본인의 이름은?? ")
    names.append(player)

    print()
    print("=======================================================")
    print()
    print()
    
    print("         본인의 주량을 선택해주세요.         ")
    print()
    print("         소주 1병은 4잔 입니다.         ")
    print()

    print("1. 반 병")
    print("2. 반 병에서 한 병")
    print("3. 한 병에서 한 병 반")
    print("4. 한 병 반에서 두 병")
    print("5. 두 병 이상")
    print()
    print()

    while True:
        select_alcohol_num = input("본인의 주량은?  ")
        if select_alcohol_num == "1" :
            max_alcohol_num=2
            break
        elif select_alcohol_num == "2":
            max_alcohol_num = 4
            break
        elif select_alcohol_num == "3":
            max_alcohol_num = 6
            break
        elif select_alcohol_num == "4":
            max_alcohol_num = 8
            break
        elif select_alcohol_num == "5":
            max_alcohol_num = 10
            break
        else:
            print("1~5 사이의 숫자를 선택해 주세요!!")
    
    print()

    while True:
        player_num = int(input("몇 명과 대결을 하시겠어요? (사회적 거리두기로 인해서 최대 3명을 초대할 수 있습니다!) : "))
        if player_num in [1,2,3]:
            out = random.sample(sorted(computer),player_num)
            max_alcohol.append(max_alcohol_num)
            for i in range(len(out)):
                names.append(out[i])
                max_alcohol.append(random.randrange(2,10,2))
            print()
            print("오늘의 상대는", names[i])
            break
        else:
            print("1에서 3 사이의 정수를 입력해주세요!")



# ----------------------- 게임 시작 -----------------------
print()
print("             혼자하는 술 게임             ")
print()
print()
print()
while True:
    answer = input(" 음주를 시작하시겠습니까? (y/n) ")
    if answer == "y":
        game_setting(names, max_alcohol)
        break
    elif answer == "n":
        print(" 담에 같이 놀아요 😢")
        exit()
    else:
        print("y 혹은 n 로 입력해주세요")



player = names[0]
game_num = input("무슨 게임? :")
print(names)

if game_num == "1":
    subway.full_subway_game(names, player)

elif game_num == "2":
    up_down.updown(player, names)

elif game_num == "3":
    Game_of_Death.start(player, names)
