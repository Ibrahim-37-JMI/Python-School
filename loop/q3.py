#wap to print all prime numbers btw 2 given no

num1=int(input('enter first number\n'))
num2=int(input('enter second number\n'))

if num1>num2:
    num1, num2 = num2, num1




for e in range(num1,num2):
    if e>1:
       for m in range(2,e):
           if e%m==0:
               break
       else:
         print(e)


           
            
            

        

