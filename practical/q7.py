#wap to print sum of even and odd no of first n numbers


num=int(input('enter the number : '))
m=0
n=0
for e in range (1,num+1):
    if e%2 == 0:
        m+=e
    else:
        n+=e

print('the sum of odd numbers is',m)
print('the sum of even numbers is',n)
        

