import random
import time

filenme="studentsdata.txt"

# file for students rigistered data that should be inserted correctlty like no convinence
def studentdatasavedfileintotxt(datainserted):
    with open(filenme ,'a+',encoding='utf-8') as fread:
        data=fread.readlines()

    data.append(datainserted)

    with open (filenme, 'a+',encoding='utf-8') as fwrite :
        fwrite.writelines(data)

# information for studensts addded for admin like who see or who not but not able to change bcz of data efficency no crrouption 
def studentinfoormation():
    with open(filenme,'r+') as fread:
        data=fread.readlines()
    
    print(data)

    



# quesstions
math_questions = [
    "What is 12 + 15?",
    "Subtract 25 from 50. What is the result?",
    "Multiply 8 by 7. What is the product?",
    "Divide 36 by 6. What is the quotient?",
    "What is the square of 9?",
    "What is 18 minus 7?",
    "Add 43 and 28. What is the sum?",
    "What is 56 divided by 8?",
    "What is 15 multiplied by 4?",
    "Find the remainder when 27 is divided by 4."
]
#  answerlist
correct_answers = [
    '27', '25', '56', '6', '81', '11', '71', '7', '60', '7'
]

# options for easy mode
options = [
    ['25', '27', '28', '30'],
    ['15', '20', '25', '30'],
    ['50', '52', '56', '60'],
    ['5', '6', '7', '8'],
    ['81', '72', '90', '100'],
    ['10', '11', '12', '13'],
    ['68', '70', '72', '75'],
    ['6', '7', '8', '9'],
    ['55', '60', '65', '70'],
    ['6', '7', '8', '9']
]

# main menu
def menu():
    print("enter 1 for admin login")
    print("enter 2 for empolyee login")
    print("enter 3 for student login")
    print("enter 0 for end programe")

    
# adminmenu
def adminmenu():
    print("enter 1 for add new quesstion")
    print("enter 2 for delete new quesstion")
    print("enter 3 for update new quesstion")
def adminaddingquesstion():
    print("enter your quesstion")
    quesstion=input()
    math_questions.append(quesstion)
    print("enter your quesstion ANSWER")
    answer=input()
    correct_answers.append(answer)
    print("add option for that quesstion")
    optionlist=[]
    for i in range(4):
        print(f"enter your option {i+1}")
        option=input()
        optionlist.append(option)
    
    options.append(optionlist)

    print("quesstion added successfully")

def adminupdatequesstion():
    print("already present quesstion are")
    for i in range(len(math_questions)):
        print(f"{i+1} in math quesstion is")
        print(math_questions[i])
    
    print("enter the number of quesstion u want to update")
   
    quesstionnumber=int(input())
    
    print("enter your quesstion")
    quesstion=input()
    math_questions[quesstionnumber]=quesstion
    print("enter your quesstion ANSWER")
    answer=input()
    correct_answers[quesstionnumber]=answer
    print("add option for that quesstion")
    optionlist=[]
    for i in range(4):
        print(f"enter your option {i+1}")
        option=input()
        optionlist[quesstionnumber]=optionlist
    

    options.append(optionlist)

def deletequesstion():
    print("already present quesstion are")
    for i in range(len(math_questions)):
        print(f"{i+1} in math quesstion is")
        print(math_questions[i])
    
    print("enter the number of quesstion u want to update")
   
    quesstionnumber=int(input())
    math_questions.pop(quesstionnumber)

#admin function
def admin():
    password=['1111','2222','3333','admin']
    enteryourpassword=input("enter your password")

    if enteryourpassword in  password:
            adminmenu()
            choice=int(input("enter your choice"))
            if choice==1:
                adminaddingquesstion()
            elif choice==2:
                adminupdatequesstion()
            elif choice==3:
                deletequesstion()
            else:
                print("invalid choice")
               
        
# empolyee function
def empolyee():
    pass

def studentdata():
    nameinput=input("enter your name")
    age=input("enter your age ")
    while True:
        emailinput = input("Enter your email: ")
        if "@" in emailinput and emailinput.endswith(".com"):
            break
        else:
            print("Invalid email! Please enter a valid email with '@' and '.com'.")

    stringdata=f"NAME is {nameinput} , Age is {age} , Email is {emailinput} "
    studentdatasavedfileintotxt(stringdata)


def studentmenu():
    print("welcome to student menu")
    print(f"1 fro easy mode")
    print('2 for hard mode')
    print("3 for exit")

def uniquenumberlist():
    unique_numbers = []

# Loop until the list contains 10 unique numbers    
    while len(unique_numbers) < 10:
        number = random.randint(0, 9)  # Generate a random number between 1 and 10

        if number not in unique_numbers:
            unique_numbers.append(number)  # Add the number if it is not already in the list
  # Print the final list of 10 unique numbers
    return unique_numbers

def easymodequesstion():
    result=0
    listfrowronganswer=[]
    # Initialize an empty list
    unique_numbers=uniquenumberlist()
    for i in range(len(math_questions)):
        number= int(unique_numbers[i])
        print(f"{i+1}   quesstion is {math_questions[number]}  \n with options \n {options[number]}")
        
        starttime= time.time()
        remaingtime =time.time()-starttime
        answer=int(input("enter our answer"))
        if(remaingtime>30):
            print("time is over ")
            continue
       
        elif answer==int(correct_answers[number]):
            result +=10
        else:
            listfrowronganswer.append(number)

    

    print(f"you score with the result of {result} out of 100 \n THE WRONG QUESSTION YOU ANSWER IS ")
    for i in range(len(listfrowronganswer)):
        number= int(listfrowronganswer[i])
        if(i>len(listfrowronganswer)):
                break
        else :
            print(f"{i+1}   quesstion is {math_questions[number]}  \n with options \n {options[number]} \n the correct answer is {correct_answers[number]}")
   
    studentdatasavedfileintotxt(datainserted=str(answer))

    print("THANK Y HAVE A NICE DAY")    

def hardmodequesstion():
    result=0
    listfrowronganswer=[]
    # Initialize an empty list
    unique_numbers=uniquenumberlist()
    for i in range(len(math_questions)):
        starttime=time.time()
        number= int(unique_numbers[i])
        print(f"{i+1}   quesstion is {math_questions[number]}  \n")
        answer=int(input("enter our answer"))
        endtime=time.time()-starttime
        if(endtime>10):
            continue
        elif answer==int(correct_answers[number]):
            result +=10
        else:
            listfrowronganswer.append(number)

    

    print(f"you score with the result of {result} out of 100 \n THE WRONG QUESSTION YOU ANSWER IS ")
    for i in range(len(listfrowronganswer)):
        number= int(listfrowronganswer[i])
        if(i>len(listfrowronganswer)):
                break
        else :
            print(f"{i+1}   quesstion is {math_questions[number]}  \n with options \n {options[number]}")
    print("THANK Y HAVE A NICE DAY")

# student function
def student():
    result=0
    studentdata()
    randomchoice=random.randint(1,10)

    studentmenu()
    choice=int(input("enter your choice"))
    if choice==1:
          easymodequesstion()
    elif choice==2:
        hardmodequesstion()
    elif choice==3:
        pass
    else:
        deletequesstion()
# main function
def main():
    print("welcome into student managment system")
    menu()
    choice=int(input("enter your choice"))
    if( choice==1):
        admin()
    elif(choice==2):
       empolyee()
    elif(choice==3):
        student()
    else:
        print("invalid choice")            

# calling menu
main()
