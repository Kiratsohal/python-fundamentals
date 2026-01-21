even=[2,4,6]
odd=[1,3,5,7]

even.extend(odd)
print(even)
even.sort(reverse=True)
print(even)
even.sort()
print(even)
another_even=even
print(another_even)

english="The quick brown fox jumps over the lazy dog"
another=sorted(english)
print(another)

x=[1.1,1.5,1.9,2.1,2.5,3.1,3.5,4.1,4.5,5.1,5.5,6.1]
another=sorted(x)
print(another)
x.sort()
print(x)

key=["john","kirat","HELLO","wick"]
key.sort()
print(key)

