
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

#          10
'''

1  1  2  1  3  1 - 9
1  2  2  2  3  2 - 12
1  3  2  3  3  3 - 15
1  4  2  4  3  4 - 18
1  5  2  5  3  5 - 21


Even place we have 111,222,333
Odd place we have 123,123,123

APPROACH 1:

n=int(input('n: '))
for i in range(1,n+1):
    print(1, 0+i, 2, 0+i, 3, 0+i)
    # print(1, 0+1, 2, 0+1, 3, 0+1)
    # print(1, 0+2, 2, 0+2, 3, 0+2)
    # print(1, 0+3, 2, 0+3, 3, 0+3)

APPROACH 2:

n=int(input('n: '))
for i in range(1,n+1):
    for j in range(1, (n//2)+2):
        print('{} {}'.format(j, i), end=' ')
    print()
'''

#             11 (Opposite version of 10)

'''

n: 5
1 1 1 2 1 3
2 1 2 2 2 3
3 1 3 2 3 3
4 1 4 2 4 3
5 1 5 2 5 3


n=int(input('n: '))
for i in range(1,n+1):
    for j in range(1, (n//2)+2):
        print('{} {}'.format(i, j), end=' ')
    print()
'''

#              12
'''

n: 5
1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25

n=int(input('n: '))
for i in range(1,n+1):
    for j in range(n):
        print(n*j+i, end=' ')
        # print(5*0+1, 5*1+1, 5*2+1)
        # print(5*0+2, 5*1+2, 5*2+2)
        # print(5*0+3, 5*1+3, 5*2+3) 
    print()

'''

#               13
'''

1 10 11 20 21
2 9  12 19 22
3 8  13 18 23
4 7  14 17 24 
5 6  15 16 25

n=int(input('n: '))

for x in range(1, n+1):
    r1 = x
    r2 = n-x+1
    for y in range(1, n+1):
        print('y = ', y, 'x = ',x)
        if(y%2 == 1):
            print('{}'.format(r1), end=' ')
        else:
            print('{}'.format(r2), end=' ')
        r1 = r1+n
        r2 = r2+n
    print()

'''
#               14
'''

3 6 9
2 5 8
1 4 7

n=int(input('n: '))
for i in range(0, n):
    for j in range(1, n+1):
        print(n*j-i, end=' ')
        # print(3*1-0, 3*2-0, 3*3-0)
        # print(3*1-1, 3*2-1, 3*3-1)
        # print(3*1-2, 3*2-2, 3*3-2)
    print()
'''

#             15
'''

3 4 9 
2 5 8
1 6 7

n=int(input('n: '))
for i in range(0, n):
    for j in range(1, n+1):
        if(j%2 == 0):
            print(n+i+1, end=' ')
        else:
            print(n*j-i, end=' ')
        # print(3*1-0, 3+0+1, 3*3-0)
        # print(3*1-1, 3+1+1, 3*3-1)
        # print(3*1-2, 3+1+2, 3*3-2)
    print()
'''

#            16

'''

1 2 3
2 3 4
3 4 5

n=int(input('n: '))
for i in range(0, n):
    for j in range(1, n+1):
        print(j+i, end=' ')
        # print(1+0, 2+0, 3+0)
        # print(1+1, 2+1, 3+1)
    print()
'''

#      print odd of 16 pattern
'''
1 3 5
3 5 7
5 7 9

n=int(input('n: '))
start = 1
end = n+n

for i in range(1, n+1):
    # print(start=1, end=6)
    # print(start=3, end=8)
    # print(start=5, end=10)
    for j in range(start, end+1):
        if j%2 != 0:
            print(j, end=' ')
            pass
    start = end-n
    end= end+n-1
    print()

'''

#                 BINARY PATTER
#                   17
'''
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0


n=int(input('n: '))
for i in range(0, n):
    for j in range(0, n):
        if i%2==0:
            if j%2==0:
                print(0, end=' ')
            else:
                print(1, end=' ')
        elif i%2 != 0:
            if j%2==0:
                print(1, end=' ')
            else:
                print(0, end=' ')
    print()

'''

#                 18
'''
n: 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1

n=int(input('n: '))
for i in range(0, n):
    for j in range(0, n):
        if i%2==0:
            if j%2==0:
                print(1, end=' ')
            else:
                print(0, end=' ')
        elif i%2 != 0:
            print(0, end=' ')
    print()

'''        

#             19

'''
n: 5
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1

n=int(input('n: '))
for i in range(0, n):
    for j in range(0, n):
        if i%2==0:
            print(1, end=' ')
        elif i%2 != 0:
            print(0, end=' ')
    print()

'''   

#                  20
'''
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0

n=int(input('n: '))
for i in range(0, n):
    for j in range(0, n):
        if j%2==0:
            print(0, end=' ')
        elif j%2 != 0:
            print(1, end=' ')
    print()

'''

#    21 Opposite version of 20

#               ABC SQUARE PATTER 22
'''
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y

n=int(input('n: '))
alphaint = 65
for i in range(n):
    for j in range(n):
        print(chr(alphaint), end=' ')
        alphaint+=1
    print()
    # print('65 66 67 68 69')
    # print('70 71 72 73 74')

'''

