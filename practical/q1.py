#wap to calc and print quadratic equations
import math
print('for quadratic equation equation, ax^w+by+c, enter the coefficients below')

a=int(input('enter the value of a :'))
b=int(input('enter the value of b :'))
c=int(input('enter the value of c :'))

dis=b**2 - 4*a*c

if dis<0:
    print('the roots are imaginary, so no real roots')
elif dis==1:    
    print('the roots are real and equal')
    root1=-b/a
    print('root 1 is',root1,'and root 2 is',root1)
else :
    print('the roots are real')
    root1=-b+math.sqrt(dis)/2*a
    root2=-b-math.sqrt(dis)/2*a
    print('root1 is',root1,'and root 2 is',root2)


