#wap to print next prime number

# num=int(input('enter the number\n'))

# num+=1
# count=0
# while count==0:
#   count=0
#   for e in range(2,num):
#     if num%e == 0:
#          count+=1
#          break
         
#   if count==0:
#       print(num)
#       break
#   else:
#       num+=1

num=int(input('enter the number\n'))
num+=1
count=0

while count==0:
    count=0
    for e in range(2,num):
        if num%e==0:
            count+=1
            break
    if count==0:
            print(num)
            break
    else:
        count=0
        num+=1       

           


         

    


  




     
     

