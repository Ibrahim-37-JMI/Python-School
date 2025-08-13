#wap to count no of repeated char

str = input('enter any string : ')
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print('count of all characters is : ',dict)

