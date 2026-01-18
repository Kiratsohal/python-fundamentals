available_parts=['cpu','ram','dvd','ssd','cd']
valid_options=[]
for i in range(1,len(available_parts)+1):
    valid_options.append(str(i))
print(valid_options)
current_choice="-"
computer_parts=[]
while current_choice !="0":
    if current_choice in valid_options:
        print('adding {}'.format(current_choice))
        index=int(current_choice)
        valid_choice=available_parts[index]
        computer_parts.append(valid_choice)
    else:
        for part,number in enumerate(available_parts):
            print("{0}: {1}".format(part+1,number))
    current_choice=input()
print(computer_parts)