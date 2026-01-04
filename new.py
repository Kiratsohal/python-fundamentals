digit=8
print('guess a number between 1-10')
guess=int(input())

if guess>digit:
    print('guess a lower number')

    guess=int(input())
    if guess>digit:
        print(" think smaller digit")

    guess=int(input())
    if guess==digit:
        print(" you are right")
    else:
        print('you have not guessed it correctly')
elif guess<digit:
    print('think a greater number')

    guess=int(input())
    if guess<digit:
        print(" think higher  digit")

        guess=int(input())
    if guess<digit:
        print(" think higher  digit")

        guess=int(input())
    if guess<digit:
        print(" think higher  digit")

        guess=int(input())
    if guess<digit:
        print(" think higher  digit")
    if guess!=digit:
        print('out of chances')
else:
    print("you guessed it on first chance")


