import random
import time

def updown(player,names):
    data=[]
    loser=[]

    names_num=len(names) ##플레이어 수

    print("===============================")
    print("      술 뚜껑 업다운 게임       ")
    print("===============================")

    print("술 뚜껑 뒤에는 1~50까지의 숫자 중 한 가지 숫자가 있습니다.")
    print("♬♪ 마시면서 배우는 술↘게→임↗ 배우면서 마시는 술↘게→임↗ ♬♪\n")

    for i in range(50):
        data.append(i+1)

    target=random.randrange(1,51)
    num=0
    start=1
    end=50

    while(1):
        if num%names_num==0:
            if start==end:
                print("한가지 숫자만 남았어요!")
            else:
                print("선택지: {} ~ {}\n".format(start,end))
            choice=int(input("▶ 한 가지 숫자를 선택하시오 : "))
        else:
            choice=random.randrange(start,end+1)
            print("{}은 {}을 선택했습니다.".format(names[num%names_num],choice))
        
        if choice == target:
            time.sleep(1)
            print("\n********************************************")
            print("이럴수가... 정답은 {} !!!!!!!!! ㄴㅇㄱ".format(target))
            print("{} 빼고 한 잔 해~".format(names[num%names_num]))
            print("마셔라 마셔라♬♪ 술이 들어간다 쭊 쭊쭊쭊쭊♬♪\n")
            print("********************************************\n")
            for i in range(names_num):
                if(i!=num%names_num):
                    loser.append(i)
                    
            return loser
            
        elif choice < target:
            print("UP\n")
            time.sleep(1)
            start=choice+1
            num+=1       
        else:
            end=choice-1
            print("DOWN\n")
            time.sleep(1)
            num+=1
    
        

