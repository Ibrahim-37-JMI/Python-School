
# i=1
# while i==7:
#  marks=int(input('enter number of student ',i))
#  i+=1

# l=[mark1,mark2,mark3,mark4,mark5,mark6]
# print(sorted(l))


# for e in list:
#     e=int(e)
#     list.append(e)

# print(list)
str=input("Enter the number separated by commas") #1,2,3,4,5

list=str.split(",") #["1","2","3",]

print(list)

for e in list:
    e=int(e)
    list.append(e)

print(list)