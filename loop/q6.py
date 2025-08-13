# wap to print n prime numbers

num=int(input('enter the number\n'))
# count=0
# while count==0:
#     count=0
#     for e in range(2,num):
#         if num%e==0:
#             count +=1
#             break
#     if count==0:
#         print (num)
#     else:
#         count=0
#         num+=1
count=0
e=2
while e<=num:
    for m in range(2,e):
        if e%m==0:    
            count+=1
            break
    if count==0:
        print (e)
        e+=1
        count=0
    else:
        count=0
        e+=1




    