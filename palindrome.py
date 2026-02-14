def first_name(string):
    return string[::-1]==string


word=input('enter your name')
if first_name(word):
    print('it is palindrome')
else:
    print('it  is not palindrome')
