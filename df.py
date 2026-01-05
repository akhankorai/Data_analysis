def cheacker(number):
    if number ==0:
        print('zero')
    elif number <0:
        print("negative")
    else :
        print('postive')

def table(number):
    for i in range (1,11):
        print (f"{i} * {number} ==   {i * number}")

def greater_commoon_devisor(number1,number2):
    comomn=0
    size=number1 if number1>number2 else number2
    for i in range (1,size):
        if number1 % i == 0 and number2 % i == 0:
            comomn = i
    print(comomn)

list=[10,30,20,40,30,50]
list.reverse()

for i in range(0,len(list),1):
    for j in range(1,len(list)-1,1):
        if(list[i]==list[j]):
            list.pop(list[j])

print(list)

def listoperations(list):
    list.sort()
    print(list)
    