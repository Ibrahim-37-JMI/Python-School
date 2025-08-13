#wap to find multiples of a no out of given 5 no
print('enter the five numbers below')

num1=int(input('enter the first number : '))
num2=int(input('enter the second number : '))
num3=int(input('enter the third number : '))
num4=int(input('enter the fourth number : '))
num5=int(input('enter the fifth number :'))

div=int(input('enter the divisor : '))
count=0
print('the multiples of',div,'are : ')
if num1%div == 0:
   print (num1)
   count+=1
if num2%div == 0:
   print (num2)
   count+=1
if num3%div == 0:
   print (num3)
   count+=1
if num4%div == 0:
   print (num4)
   count+=1
if num5%div == 0:
   print (num5)
   count+=1
print(count,'multiples of',div,'found')







