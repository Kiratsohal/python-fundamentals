import random
number=random.randint
highest=10
print=int(input('guess a number between 1-{}'.format(highest)))
guess=int(input())

if guess<number:
    print('you need to think for a higher number')
    guess=int(input())
    if guess==number:
     print('you are right')
    else:
       print('wrong guesss')

elif guess>number:
    print('guess a lower number')
    guess=int(input())
    if guess==number:
        print('you are right')
    else:
       print('not today')
else:
   print('guessed on first time')
