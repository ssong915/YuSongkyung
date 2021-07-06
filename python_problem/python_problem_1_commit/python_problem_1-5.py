import re


def get_input():
    while(1):    
        input_num=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")        
        
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        it_is = re.match(num_format,input_num)

        if(it_is):
            input_num=int(input_num)
            if(1<=input_num<=3):
                break
            else:
                print("1,2,3 중 하나를 입력하세요")
        else:
            print("정수를 입력하세요")

    return input_num

num=0

print_num=get_input()
for _ in range(print_num):
            num += 1
            print('player A:', num)

print_num=get_input()
for _ in range(print_num):
            num += 1
            print('player B:', num)