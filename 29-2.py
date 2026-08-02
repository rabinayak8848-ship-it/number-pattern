num=9
if num%2!=0:
    for row in range(1,num+1):
        for col in range(1,num+1):
            if (row==1 or col==1 or row==num or col==num or row== num //2+1 or col== num//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print( )
else:
    print('not a odd number')
print('--------------------------------------------------')
num=9
if num%2!=0:
    for row in range(1,num+1):
        for col in range(1,num+1):
            if (row==1 or col==1 or row==num or col==num or row== num //2+1 or col== num//2+1 or row+col==num+1 or row == col):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print( )
else:
    print('not a odd number')
print('-----------------------------')
num=9
for row in range(1,num+1):
        for col in range(1,num+1):
            if (row==1 or col==1 or row==num or col==num or (row==num//2 +1 and col==num//2 +1) ):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print( )

    

