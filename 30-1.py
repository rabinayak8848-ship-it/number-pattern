print( '1st program------------')

num=4
space=num-1
star=1
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        print('*', end=' ')
    print( )
    space=space -1
    star= star +2
space=1
star=(2*num)-3
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        print('*', end=' ')
    print( )
    space=space +1
    star= star -2 
print( '2nd program------------')

num=4
space=num-1
star=1
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star :
          print('*', end=' ')
        else:
            print(' ',end=' ')
    print( )
    space=space -1
    star= star +2
space=1
star=(2*num)-3
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star:
          print('*', end=' ')
        else:
            print(' ',end=' ')
        
    print( )
    space=space +1
    star= star -2
print('3rd----------------------')
num=4
space=num-1
star=1
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star or (col2 == star //2 + 1 and row == num):
          print('*', end=' ')
        else:
            print(' ',end=' ')
    print( )
    space=space -1
    star= star +2
space=1
star=(2*num)-3
for row in range( 1,num):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star or row == num:
          print('*', end=' ')
        else:
            print(' ',end=' ')
        
    print( )
    space=space +1
    star= star -2
print( '4th program------------')
num=4
space=num-1
star=1
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if (col2==1 or col2==star or row == num):
          print('*', end=' ')
        else:
            print(' ',end=' ')
    print( )
    space=space -1
    star= star +2
space=1
star=(2*num)-3
for row in range( 1,num):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star or row == num:
          print('*', end=' ')
        else:
            print(' ',end=' ')
        
    print( )
    space=space +1
    star= star -2
print('5 th program-------------------------')
num=4
space=num-1
star=1
for row in range( 1,num+1):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if (col2==1 or col2==star or row == num or col2==(star+1)//2):
          print('*', end=' ')
        else:
            print(' ',end=' ')
    print( )
    space=space -1
    star= star +2
space=1
star=(2*num)-3
for row in range( 1,num):
    for col1 in range(1, space+1):
        print(' ', end=' ')
    for col2 in range(1,star+1):
        if col2==1 or col2==star or row == num or col2==(star+1)//2:
          print('*', end=' ')
        else:
            print(' ',end=' ')
        
    print( )
    space=space +1
    star= star -2

