available_options=['cpu',
                   'ram',
                   'dvd',
                   'pc',
                   'ssd']
current_choice="-"
computer_parts=[]

while current_choice !="0":
    if current_choice in"12345":
        print('adding {}'.format(current_choice))
        if current_choice=="1":
            computer_parts.append('cpu')
        elif current_choice=="2":
            computer_parts.append('ram')
        elif current_choice=='3':
            computer_parts.append('dvd')
        elif current_choice=='4':
            computer_parts.append('pc')
        elif current_choice=='5':
            computer_parts.append('ssd')
        
    else:
      for number, parts in enumerate(available_options):
          print('{0}: {1}'.format(number+1,parts))
    current_choice=input()
print(computer_parts)

for x,y in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print(x,y)