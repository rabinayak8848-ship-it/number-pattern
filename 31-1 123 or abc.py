num=4

for row in range(1,num+1):
    for col in range(1,num+1):
        print(row, end=' ')
    print( )
print('-----------------2')
num=4

for row in range(num,0,-1):
    for col in range(1,num+1):
        print(row, end=' ')
    print( )
print('-----------------3')
num=4

for row in range(1,num+1):
    for col in range(1,num+1):
        print(col, end=' ')
    print( )
print('-----------------4')
num=4

for row in range(1,num+1):
    for col in range(num,0,-1):
        print(col, end=' ')
    print( )
print('-----------------5')
num=5

for row in range(1,num+1):
    for col in range(1,row+1):
        print(col, end=' ')
    print( )
print('-----------------6')
num=5

for row in range(1,num+2):
    for col in range(1,row):
        print(col, end=' ')
    print( )
print('-----------------7')
num=5

for row in range(num+1,1,-1):
    for col in range(1,row):
        print(col, end=' ')
print('-----------------8')
num=5

for row in range(1,num+1):
    for col in range(row,0,-1):
        print(col, end=' ')
    print( )
print('-----------------9')
num=5

for row in range(num,0,-1):
    for col in range(row,0,-1):
        print(col, end=' ')
    print( )
print('-----------------10')
num=5

for row in range(num,0,-1):
    for col in range(row,num+1):
        print(col, end=' ')
    print( )
print('-----------------11')
num=5
space=num-1
for row in range(num,0,-1):
    for col1 in range(1,space+1):
        print(' ',end=' ')
    for col2 in range(row,num+1):
        print(col, end=' ')
    print( )
    space=space-1
print('-----------------12')
num=5
space=num-1
for row in range(1,num+1):
    for col1 in range(1,space+1):
        print(' ',end=' ')
    for col2 in range(row,0,-1):
        print(col2, end=' ')
    print( )
    space=space-1
print('-----------------13')
num=5
space=0
for row in range(0,num+1):
    for col1 in range(1,space+1):
        print(' ',end=' ')
    for col2 in range(num,row,-1):
        print(col2, end=' ')
    print( )
    space=space+1












    
    
