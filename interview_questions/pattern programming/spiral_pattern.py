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

n=int(input('n: '))

right=n-1
left=0

dp=[[0]*n for i in range(n)]

for i in range(left, right):
    dp[0][i] = i+1

for i in range(n):
    dp[i][n-1]=n+i

value = n+n+len(dp[n-1][:n-2])
for i in range(n-1):
    dp[n-1][i] = value
    value-=1

top=1
bottom=n-1
value = bottom-1
for i in range(top, bottom):
    value += 1
for i in range(top, bottom):
    dp[i][0] = n+n+value
    value-=1

value = dp[1][0]+1
for i in range(1,n-1):
    dp[1][i] = value
    value+=1

value = dp[1][n-2]+1
for i in range(2,n-1):
    dp[i][n-2]= value
    value+=1

value = dp[3][n-2]+2
for i in range(1,n-2):
    dp[3][i]= value
    value-=1

value = dp[3][1]+1
for i in range(1,n-2):
    dp[2][i]= value
    value+=1

for i in range(n):
    #print(' '.join(dp[i]), end='/n')
    print(' '.join(str(j) for j in dp[i]), end='\n')
