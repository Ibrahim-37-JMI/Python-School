
num=int(input('enter the natural number \n'))
'''
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1

if count==2:
    print('number is prime')
else:
    print('number is not prime')       
      
'''
count=0
i=2
while i<=num-1:
    if num%i==0:
        count=1
    i+=1
if count==1 :
    print('number is not prime')
else:
    print('number is prime')    
