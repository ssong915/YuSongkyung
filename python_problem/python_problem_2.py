def Menu1(student) :
    try:
        name,mid,final=input("Enter name mid-score final-score : ").split()
        if((float(mid)-round(float(mid)))!=0 or (float(final)-round(float(final)))!=0):
            print("Score is not positive integer!")
            return

        if (name in student) == True:
            print('Already exist name!')   
            return     
        
        mid=int(mid)
        final=int(final)
        grade=0
        student[name] = [mid, final,grade]
    
    except ValueError : 
        print("Num of data is not 3!")
            

def Menu2(student):
    for key, value in student.items():
        avg=(value[0]+value[1])/2
        if(avg>=90):
            value[2]='A'
        elif(avg>=80):
            value[2]='B'
        elif(avg>=70):
            value[2]='C'
        else:
            value[2]='D'
    print ("Grading to all students.")

def Menu3(student) :
    for key, value in student.items():
        if value[2]==0:
            print("There is a student who didn't get grade.")
            return

    print("\n---------------------------------")
    print("name     mid     final       grade")
    print("---------------------------------")
    for key, value in student.items():
        print(f'{key:<10s}{value[0]:<10d}{value[1]:<10d}{value[2]:<10s}')

def Menu4(student):
    del_student=input("Enter the name to delete: ")  
    if (del_student in student):
        del student[del_student]
        print(del_student,' student information is deleted.')
    else:
        print("Not exist name!")


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
student=dict()
while True:
    try:
        choice = int(input("Choose menu 1, 2, 3, 4, 5 : "))    
        if choice == 1:            
            Menu1(student)

            
        elif choice==2:        
            if not student:
                print ("No student data!")
            else:      
                Menu2(student)

        elif choice==3:
            if not student:
                print ("No student data!")
            else:
                Menu3(student)

        elif choice==4:           
            if not student:
                print ("No student data!")
            else:
                Menu4(student)

        elif choice==5:
            print("Exit Program!")
            break

        else:
            print("Wrong number. Choose again.")
    except:
        print("Wrong number. Choose again.")


