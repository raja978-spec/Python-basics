
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

