num=int(input('enter the number '))
temp=num
res=0
length=len(str(num))
while num>0:
    rem=num%10
    res= res+rem**length
    num=num //10
    length= length - 1
if temp== res:
    print('number  is disarium number')
else :
    print('number is not disarium number')
