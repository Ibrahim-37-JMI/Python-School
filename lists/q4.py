# wap to return 2nd largest no

integer = input('Enter a list separated by spaces : ').split()
no=[]
for num in integer:
    no.append(int(num))
    
number=no
 
largest = number[0]
for num in number[1:]:
    if num>largest:
        largest=num
seclar=number.remove(largest)
larger=seclar[0]
for gum in seclar:
    if gum > larger:
        larger=gum


      
print (larger)
 