import random
import time

def start(player, names):
    print(len(names))

    member_num_matrix=[]

    picked_matrix=[]

    print("---------------------------")
    print("-----The Game of Death-----")
    print("---------------------------")

    print("※참가자: ", end="")
    print(names)


    Flag=True
    while Flag:

        num=0
        selected = input("※본인을 제외한 두 명을 골라주세요~~ (name1 name2): ").split()
        if len(selected) != 2 : 
            print("※두 명을 골라주세요!")
            continue
        if selected[0]==selected[1] : 
            print("※서로 다른 두 명을 골라주세요!")
            continue

        for i in range(1,len(names)):
            if names[i]==selected[0]:
                num+=1
                a=i
            if names[i]==selected[1] :
                num+=1
                b=i

        if(num==2): 
            picked_matrix.append([selected[0], selected[1]])
            member_num_matrix.append([a,b])
            Flag=False

    for i in range(1,len(names)):
        a=random.randint(0,len(names)-1)
        b=random.randint(0,len(names)-1)

        while a==i or b==i or a==b:
            a=random.randint(0,len(names)-1)
            b=random.randint(0,len(names)-1)

        picked_matrix.append([names[a], names[b]])
        member_num_matrix.append([a,b])

    print("\n---------------------------\n")
    for i in range(len(names)):
        print(names[i]+"(이)가 지목한 사람: "+picked_matrix[i][0]+", "+picked_matrix[i][1])

    time.sleep(1)
    print("\n---------------------------\n")
    if player==names[0]:
        numflag=False
        while not numflag:
            countnumber=input("※원하는 숫자를 불러주세요(1 이상): ") 
            if countnumber.isnumeric() and int(countnumber)>=1:
                countnumber=int(countnumber)
                numflag=True
    else:
        countnumber=random.randint(1,30)

    print(member_num_matrix)

    print("\n---------------------------\n")
    print("=========게임 시작===========")
    print("\n---------------------------\n")
    time.sleep(1)


    for i in range(len(names)):
        if player==names[i]:
            myturn=i
    print(str(countnumber)+" "+names[myturn])

    while countnumber>0:
        time.sleep(0.2)
        if myturn==0:
                select_one=input("※본인이 고른 두 사람 중에 한 명 골라!: ")
                while select_one != picked_matrix[0][0] and select_one != picked_matrix[0][1] :
                    select_one=input("※본인이 고른 두 사람 중에 한 명 골라!: ")

                if select_one == picked_matrix[0][0]:
                    countnumber-=1
                    print(countnumber, end="")
                    pick=0
                    myturn = member_num_matrix[0][pick]
                    print(names[myturn])
                elif select_one == picked_matrix[0][1]:
                    countnumber-=1
                    print(countnumber, end=" ")
                    pick=1
                    myturn = member_num_matrix[0][pick]
                    print(names[myturn])

        else:
            countnumber-=1
            ranpick=random.randint(0,1)
            print(countnumber, end=" ")
            myturn=member_num_matrix[myturn][ranpick]
            print(names[myturn])


    print("\n---------------------------\n")
    print("=========Game Over===========")
    print("\n---------------------------\n")
    print(names[myturn]+" 마셔!")


    #start("현주", ["건웅", "진혁", "송경", "현주", "사랑"])