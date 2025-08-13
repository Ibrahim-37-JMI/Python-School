#wap to check if 2 no are co-prime
num1=int(input('enter first number\n'))
num2=int(input('enter second number\n'))
count1=0
count2=0
if num1==num2 :
    print (num1, num2 ,  'are not co-prime')
if num1!=num2 :   
 for e in range(2, num1): 
    if num1%e==0:
        count1+=1  
   

 for e in range(2,num2): 
    if num2%e==0:
        count2+=1 


 if count1==0 and count2==0:
    print (num1, num2, 'are co-prime') 
 else:
    print (num1, num2, 'are not co-prime')           








