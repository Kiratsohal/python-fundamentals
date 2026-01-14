current_choice="-"
computer_parts=[]

while current_choice !="0":
    if current_choice in"123456":
        print("adding {}".format(current_choice))
    if current_choice=="1":
        computer_parts.append("cpu")
    elif current_choice=="2":
        computer_parts.append('ram')
    elif current_choice=="3":
        computer_parts.append('dvd')
    elif current_choice=="4":
        computer_parts.append('pc')
    elif current_choice=="5":
        computer_parts.append('laptop')
    elif current_choice=="6":
        computer_parts.append('ssd')
    else:

        print('choose options given below:')
        print("1.cpu")
        print('2.ram')
        print('3.dvd')
        print('4.pc')
        print('5.laptop')
        print("6.ssd")
    current_choice=input()
print(computer_parts)
a=input('yo have added {} . click y if it is correct or press n if incorrect'.format(computer_parts))
if a=="y":
    print('ok')
elif a=="n":
    print('oh noooo')
else:
    print('by')