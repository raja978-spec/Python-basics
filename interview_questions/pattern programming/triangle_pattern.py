#             1
'''

no=int(input('no: '))
for i in range(1,no+1):
    print(' '*(no-i) + '*' * i)

     *
    **
   ***
  ****
 *****
******
'''

#           2
'''

no=int(input('no: '))
for i in range(1,no+1):
    print(' '*(no-i), '*' * (i*2-1))

    # print(' '*4-1=3, '*'*1)
    # print(' '*4-2=2, '*'*3)
    # print(' '*4-3=1, '*'*5)
    # print(' '*0, '*'*7)


   *
  ***
 *****
*******


'''

#                         3
'''

no=int(input('no: '))
for i in range(1,no+1):
    print(' '*(no-i), '*' *i)
    # print(" "*6-1=5, '*'*1)
    # print(' '*6-2=4)

     *
    **
   ***
  ****
 *****
******
'''

#                   4
'''

no=int(input('no: '))
for i in range(1,no+1):
    print(' '*(i-1), '*' *(no*2-(i*2-1)))
    # print(' '*(1-1) = 0)  ,  '*'*  3*2- 1=5 )
    # print(' '*(2-1) = 1)   ,  '*'* 3*2- 3 =3 )
    # print(' '*(3-1) = 2)   ,  '*'* 3*2- 5 =1)


no: 4
 *******
  *****
   ***
    *

'''
# no=int(input('no: '))
# for i in range(1,no+1):
#     print(' '*(i-1), '*' *(no*2-(i*2-1)))
#     # print(' '*(1-1) = 0)  ,  '*'*  3*2- 1=5 )
#     # print(' '*(2-1) = 1)   ,  '*'* 3*2- 3 =3 )
#     # print(' '*(3-1) = 2)   ,  '*'* 3*2- 5 =1)


#                 5
'''
E
E D
E D C
E D C B
E D C B A

n=int(input('n: '))
start_alphabet_range= 65
end_alphabet_range= start_alphabet_range+n-1
for i in range(n):
    for j in range(i+1):
        # print('70')
        # print('70 69')
        # print('70 69 68')
        print(chr(end_alphabet_range-j), end=' ')
    print()
'''

#                   6
'''
    E
   DD
  CCC
 BBBB
AAAAA   

n=int(input('n: '))
aplhabet_range = 65+n
for i in range(1, n+1):
    print(' '*(n-i), chr(aplhabet_range-1)*i)
    aplhabet_range-=1
'''