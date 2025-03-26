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
no=int(input('no: '))
for i in range(1,no+1):
    print(' '*(i-1), '*' *(no*2-(i*2-1)))
    # print(' '*(1-1) = 0)  ,  '*'*  3*2- 1=5 )
    # print(' '*(2-1) = 1)   ,  '*'* 3*2- 3 =3 )
    # print(' '*(3-1) = 2)   ,  '*'* 3*2- 5 =1)


