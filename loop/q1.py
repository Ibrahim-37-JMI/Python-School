num=int (input('enter a natural number\n'))
count=0
for e in range (2,num):
    if num%e == 0:
        count+=1
    
        

if count>=1:
    print ('the number is not prime')
else:
    print ('the number is prime')