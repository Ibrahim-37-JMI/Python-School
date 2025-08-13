# # num = int(input('Enter a number : '))

# # for i in range(0,num):
n = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
 
string = input('enter')

st=string.replace(' ','')

if st==st[::-1]:
    print('palindrome')
else:
    print('no palindrome')
        


