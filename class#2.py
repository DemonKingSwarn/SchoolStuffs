x="Hello"
print(x[0])

'''
OUTPUT:-
prints the alphabet at index 0, in this case it is H.
'''

x="Lovejeet"
for i in x:
    print(i)

x="Lovejeet"
for i in range(len(x)):
    print(x[i])

'''
These are the 2 ways to traverse a string.
'''

x="Lovejeet"
print(x[2:4])

'''
OUTPUT:-
ve
'''

x="Lovejeet"
print(x[2:5:2])

'''
OUTPUT:-
vj
'''

x="Lovejeet"
print("L" in x)
print("I" in x)
print("L" not in x)
print("I" not in x)

'''
OUTPUT:-
True
False
False
True
'''

X="Love"
Y="Jeet"
print(X+Y)

'''
OUTPUT:-
LoveJeet
'''

X="Love"
Y=2
print(X*Y)

'''
OUTPUT:-
LoveLove
'''

print(ord("A"))
print(chr(90))

'''
OUTPUT:-
65
Z
'''
