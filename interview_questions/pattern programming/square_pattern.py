
#           1
'''

no=int(input('no: '))
for i in range(1,no+1):
    print('*'*no)

OUTPUT:

***
***
***
'''

#                    2
'''

no=int(input('no: '))
for i in range(1,no+1):
    print(f'{i}'*no)

no: 3
111
222
333

'''

#                      3
'''

no=int(input('no: '))
for i in range(1,no+1):
    for j in range(1,no+1):
        print(j, end='')
    print()

no: 5
12345
12345
12345
12345
12345
'''

#                   4
'''


no=int(input('no: '))
for i in range(1, (no**2)+1):
    print(i, end=' ')
    if i % no == 0:
        print()

1 2 3
4 5 6
7 8 9

'''

#                      5
'''

no=int(input('no: '))
for i in range(no, 0, -1):
    for j in range(no, 0, -1):
        print(j, end=' ')
    print()

4 3 2 1 
4 3 2 1
4 3 2 1
4 3 2 1
'''

#                      6
'''


1 4 7
2 5 8
3 6 9

3*0+1 = 1
3*1+1 = 4
3*2+1 = 7

3*0+2 = 2
3*1+2 = 5
3*2+2 = 8

3*0+3 = 3
3*1+3 = 6
3*2+3 = 9

no=int(input('no: '))
for i in range(1, no+1):
    for j in range(no):
        print(no*j+i, end=' ')
    print()
 
'''

#                   7 (ODD Square pattern)
'''

1 3 5 7
9 11 13 15
17 19 21 23
25 27 29 31


0*2+1 = 1
1*2+1 = 3
2*2+1 = 5
3*2+1 = 7 
4*2+1 = 9
5*2+1 = 11

n=int(input('n: '))
start = n
for i in range(n):
    for j in range(start-n, start):
        print(j*2+1, end=' ')
    print()
    start+=n

'''

#            8 (Even square)
'''

0*2+2 = 2
1*2+2 = 4
2*2+2 = 6

n=int(input('n: '))
start = n
for i in range(n):
    for j in range(start-n, start):
        print(j*2+2, end=' ')
    print()
    start+=n

'''

#                     9
'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

n=int(input('n: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j*i, end=' ')
    print()

'''
n=int(input('n: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j*i, end=' ')
    print()
