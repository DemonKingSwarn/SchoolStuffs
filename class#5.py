x=[1,2,3,4]
for i in range(len(x)):
    print(i)

'''
OUTPUT:-
0   1   0   1
1   2   1   2
2   3   2   3
3   4   3   4
4   5   4   5
    6   5
'''

x=[1,2,3,4,5]
a=x.copy()
print(id(a))
print(id(x))

'''
OUTPUT:-
copies the list x on a and prints the memory location where they are stored.
'''

p=[1,2,3,4,[45,55,66],"AABC",["ABC",3,4]]
print(p[-1][-1])

'''
OUTPUT:-
4
'''
