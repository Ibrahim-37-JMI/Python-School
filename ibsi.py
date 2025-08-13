# p=float(input('enter the principal amout of interest\n'))
# r=float(input('enter the rate of interest\n'))
# t=float(input('enter the time period\n'))
# SI =p*r*t/100
# print ('the simple interest is', SI)


# '''
# def nev(n):
 
#   evno = (2*e for e in range (1,n))
#   return evno
# num=int(input('enter the natural number\n'))        

# print ('first',num,'even numbers are',nev(num))
# '''

# num = int(input('Enter the number : '))
# count=0
# for e in range (2,num):
#     if num%e == 0:
#         count+=1 
# if count > 0:
#     print (num,'is not prime')
# else:
#     print (num,'is prime')    

# num = int(input('Enter the number : '))
# odd=0
# even=0
# for e in range (2,num):
#     if e%2==0:
#         even+=e
#     else:
#         odd+=e
# print('Sum of odd numbers is',odd) 
# print('Sum of even numbers is',even) 

x=int(input('enter the no'))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print(x,'is not prime')
else:
    print(x,'is prime')
    
    
                

            