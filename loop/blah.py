# Program to calculate HCF (GCD) of two numbers

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if a > b:
    a, b = b, a

while b != 0:
    temp = b
    b = a % b
    a = temp

print(f'The HCF of the entered numbers is {a}')
