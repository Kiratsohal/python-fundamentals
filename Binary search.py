low=1
high=1000
print('think of a number between {} and {}: '.format(low,high))
input("press enter to start this game")

guess=1
while True:
    guess= low+(high-low)//2
    high_low=input('my guess is {} should i guess any other number?'
              ' press h for higher number or press l for lower number or press c if number is corect'
              .format(guess)).casefold()
    if high_low=="h":
        low = guess+1
    elif high_low=="l":
        high = guess-1
    elif high_low=="c":
     print("i got it in {} times".format(guess))
     break
    else:
          print("press h or l or c  to start the game")

    guess= guess+1
