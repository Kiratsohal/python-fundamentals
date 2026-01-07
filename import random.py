import random
highest=10
number=random.randint(1,highest)
print('guess a number between 1-{}'.format(highest))

guess=int(input())
if guess==number:
    print('you guessded it on first time')
else:
    print('you have not guessed it coreectly')
    guess=int(input())
    while guess<number:
      if guess<number:
        print('think of a higher number')
    else:
        print('sorry you failed to guess it')
    if guess>number:
        print('think of a lower number')
    else:
        print('sorry you failed to guess it')
    
