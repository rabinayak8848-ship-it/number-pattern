num=7
space=num-1
star=2
for row in range(1, num+1):
    for col2 in range(1,star+1):
        print('*', end=' ')
    for col1 in range(1, space+1):
        print(' ',end=' ')
    for col2 in range(1,star+1):
        print('*', end=' ')
    if row < num//2+1:
        space=space+1
        star=star-2
    else:
        space=space -1
        star=star+2
        
         
        
    
    
