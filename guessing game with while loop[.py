import random
highest=10
number=random.randint(1,highest)
print(number)
guess=0
print('guess a number between 1-{}'.format(highest))
while guess!=number:
    guess=int(input())
    if guess==number:
        print('you guessed it')
    else:
        if guess<number:
            print('think of a higher number')
        else:
            print('think of a lower number')
    
        # if guess>number:
            
            # print('think of a lower number')

        # else:
            # print('sorry you failed to guess it')
        