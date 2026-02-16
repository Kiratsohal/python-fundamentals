def is_k(string):
      return string[::-1].casefold()==string.casefold()


def palindrome_sentence(sentence):
    string=""
    for char in sentence:
        if char.isalnum():
            string+=char
    print(string)


    #return string[::-1].casefold()==string.casefold()
    return is_k(string)



word=input('please enter a word to check')
if palindrome_sentence(word):
    print("'{} is a palindrum".format(word))
else:
    print("'{} is not a palindrum".format(word))

