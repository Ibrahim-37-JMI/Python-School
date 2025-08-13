#wap to check whether a umber is prime or not

num=int(input('enter a number\n'))
if num%1==0 and num%num==0 :

    print(num,'is prime')
else:
    print(num,'is not prime')    
