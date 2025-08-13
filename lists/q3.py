# wap to to print largest number

integer = input('Enter a list separated by spaces : ').split()
no=[]
for num in integer:
    no.append(int(num))
    
number=no
 
largest = number[0]
for num in number[1:]:
    if num>largest:
        largest=num
print (largest) 

