i=0
while i<20:
    print('i is now {0}'.format(i))
    i=i+1


directions=['north','south','east','west']
where=""
while where not in directions:
    where=input('chosse a directions')
    if where=="quit":
        print('game over')
    break
print('so you want to  {}'.format(where))