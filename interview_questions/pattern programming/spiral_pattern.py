#                 1
'''
 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9



'''

#                 2
'''
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25

n=int(input('n: '))

start, end, step, extra = 1, n+1, 1, 1 
for i in range(n):
    #print(i, start, end)
    for j in range(start, end, step):
        if i%2 == 0:
            print(j, end=' ')
        else:
            print(j, end=' ')    
    print()
    if i%2 == 0:
        start = end + n - 1
        end = start - n
        step = -1
    else:
        start = start + 1 
        end = start + n
        step = 1

'''
    