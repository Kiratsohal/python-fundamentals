available_part=["a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g"
                ]
valid_choices=[]

for i in range(1,len(available_part)+1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice="-"
computer_parts=[]

while current_choice != "0":
    if current_choice in valid_choices:
        index= int (current_choice) -1
        valid_options=available_part[index]
        if valid_options in computer_parts:
            computer_parts.remove(valid_options)
            print('removing {}'.format(current_choice))
        else:
            print('adding {}'.format(current_choice))
            computer_parts.append(valid_options)
            print('your list noe contains {}'.format(valid_options))

    else:
        print('select options given below')
        for number,part in enumerate(available_part):
            print("{} {}".format(number+1,part))

    current_choice=input()
print(computer_parts)

