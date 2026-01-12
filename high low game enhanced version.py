low=1
high=1000
print('think of a number between {}and {}' .format(low,high))
input('press enter to start')

guesses=1
while low !=high:
    guess= low+(high-low)//2
    high_low=input(' my guess is {} press h or l for higher or lower number or c if my number is correct'.format(guess)).casefold()
 
    if high_low=="h":
         low = guess+1

    elif high_low=="l":
         high = guess-1

    elif high_low=='c':
        print('i got in {} guesses'.format(guess))

        break
    else:
        print('press h or l or c')
    guesses+=1
else:
    print('you think of a number {}'.format(low))
    print('i got it in {}'.format(guesses))