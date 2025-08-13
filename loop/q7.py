# wap to calculate hcf of two no

a=int(input('enter first number \n'))
b=int(input('enter second number \n'))

if a>b:
    a,b = b,a
c=5
while c!=0:
   c = a%b
   a=b
   b=c
  
print  (a)






