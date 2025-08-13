# # # # # # # # # # # # # # # # # # l=[2,34,10,56,82,2,10,56,"ibrahim"]
# # # # # # # # # # # # # # # # # # print(l.index(56))


# # # # # # # # # # # # # # # # # l1=[34,7,89,56,98,21,7]
# # # # # # # # # # # # # # # # # # l2=[21,24,67,89,56,23,12,45,7]
# # # # # # # # # # # # # # # # # # l3=[13,233,445,66,89,2,12,446,665,3443,23,]
# # # # # # # # # # # # # # # # # # print(l1)
# # # # # # # # # # # # # # # # # # var=l1.index(98)
# # # # # # # # # # # # # # # # # # print (var)
# # # # # # # # # # # # # # # # # # l1.append(23)
# # # # # # # # # # # # # # # # # print(l1.count(7)


# # # # # # # # # # # # # # # # num=int(input("Enter the number of fruits you want to insert"))
# # # # # # # # # # # # # # # # list=[]
# # # # # # # # # # # # # # # # for i in range(1,num+1):
# # # # # # # # # # # # # # # #     fruit=input("Enter fruit name")
# # # # # # # # # # # # # # # #     list.append(fruit)

# # # # # # # # # # # # # # # # print(list)

# # # # # # # # # # # # # # # num=int(input("Enter the numbers"))
# # # # # # # # # # # # # # # l=[]
# # # # # # # # # # # # # # # for i in range(1,num+1):
# # # # # # # # # # # # # # #     num1=int(input())
# # # # # # # # # # # # # # #     l.append(num1)


# # # # # # # # # # # # # # # leven=[]
# # # # # # # # # # # # # # # lodd=[]
# # # # # # # # # # # # # # # for e in l:
# # # # # # # # # # # # # # #     if(e%2==0):
# # # # # # # # # # # # # # #         leven.append(e)
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         lodd.append(e)

            
# # # # # # # # # # # # # # # print(lodd,leven)

# # # # # # # # # # # # # # list=[10,23,42,10,7,3,33,49,100]

# # # # # # # # # # # # # # key=int(input("Enter the number you want to search in the list"))

# # # # # # # # # # # # # # for e in list:
# # # # # # # # # # # # # #     if(key==e):
# # # # # # # # # # # # # #         print("key found at index = ",list.index(e))
# # # # # # # # # # # # # #         exit()
        
# # # # # # # # # # # # # # print("key not found")


# # # # # # # # # # # # # #to finding max and min number in the list

# # # # # # # # # # # # # list=[10,23,42,10,7,3,33,49,100]

# # # # # # # # # # # # # max=list[0]

# # # # # # # # # # # # # for e in list:
# # # # # # # # # # # # #     if(e>max):
# # # # # # # # # # # # #         max=e

# # # # # # # # # # # # # print(max)


# # # # # # # # # # # # list1=[1,2,5,10]
# # # # # # # # # # # # list2=[1,2,67,89]
# # # # # # # # # # # # list3=[1,2,34,56]

# # # # # # # # # # # # for e,i,j in zip(list1 ,list2,list3):
# # # # # # # # # # # #     if(e!=i):
# # # # # # # # # # # #         print(list1.index(e))
# # # # # # # # # # # #         exit()

# # # # # # # # # # # #nested list

# # # # # # # # # # # list=[1,2,3,4,[10,20]]
# # # # # # # # # # # print(list[4][0])
# # # # # # # # # # # print(list[4][1])
# # # # # # # # # # # print(list[4])
# # # # # # # # # # # # print(list[2])

# # # # # # # # # # # list=[1,2,[2,3],5,[10,20]]
# # # # # # # # # # # print(list[2][1])
# # # # # # # # # # # print(list[4][1])

# # # # # # # # # # #string
# # # # # # # # # # str="osama"
# # # # # # # # # #     #01234

# # # # # # # # # # print(str[3])
# # # # # # # # # # print(str)
# # # # # # # # # # for e in str:
# # # # # # # # # #     print(e)


# # # # # # # # # s1="osama "
# # # # # # # # # s2="is teaching"
# # # # # # # # # s3=" python"
# # # # # # # # # print(s1+s2+s3)
# # # # # # # # # print(s1*3)

# # # # # # # # # # l1=[1,10,20]
# # # # # # # # # # l2=[3,9,10]
# # # # # # # # # # print(l1>l2)

# # # # # # # # # s1="ibrahim"
# # # # # # # # # s2="osama"
# # # # # # # # # print(s1>s2)

# # # # # # # # s="osama ghazi"
# # # # # # # # print(s.index("a"))
# # # # # # # # print(s.index("azi"))
# # # # # # # # print(s.count("am"))
# # # # # # # # print(s.startswith("ama"))
# # # # # # # # print(s.endswith("azi"))
# # # # # # # # print(s.endswith("azi"))

# # # # # # # # s="1234a"
# # # # # # # # print(s.isdigit())
# # # # # # # # print(s.isalnum())
# # # # # # # # s="abcs"
# # # # # # # # print(s.isalpha())
# # # # # # # # print(s.islower())
# # # # # # # # a="ABCSs"
# # # # # # # # print(a.isupper())


# # # # # # # s="osama"
# # # # # # # print(s.upper())
# # # # # # s="myself"
# # # # # # print(s.replace("my","hi"))

# # # # # s="{} am {} python "
# # # # # s1=s.format("I","learning")
# # # # # print(s1)

# # # # # print("{3} kaii {1} jsjs {2}kaja {0}".format(1,2,10,"osmaa"))

# # # # # str="I am teaching python"
# # # # # print(str.split(" ")) 

# # # # str=input("Enter the number separated by commas") #1,2,3,4,5

# # # # list=str.split(",") #["1","2","3",]

# # # # print(list)

# # # # l=[]
# # # # for e in list:
    
# # # #     l.append(int(e))

# # # # print(l)

# # # # list=["1","2","3","4"]
# # # # s="-"
# # # # print(s.join(list))
# # # # print(" ".join(list))
# # # # print("".join(list))


# # # s="osama"
# # #   #01234
# # # print(s[0:5:1]) 
# # # print(s[2:5:1])
# # # print(s[10:2:-1])


# # # #strobject[beg:end:step]

# # # # print(s[:2:-1])
# # # # print(s[3::-1])

# # # print(s[::-1])

# # # print([1,2,3,8,7][::-1])


# # #check string is pllindrome or not

# # str=input("Enter string")

# # temp=str

# # if(temp==str[::-1]):
# #     print("pallindrome")
 
# # else:
# #     print("not")

# str="OSAMA TEACHES ME PYTHON"
# #"PYTHON ME TEACHES OSAMA"

# list=str.split(" ") 
# list=list[::-1]
# list=" ".join(list)
# print(list)
# list=['p','r','o','b','l','e','m']
# list[1:3]=[]
# print(list)
# list[2:5]=[]
# print(list)

# s="osama teaches python"

# list=s.split(" ")
# for e in list:
#     print(e)
#     print(len(e))

s1='mysirg education services'

l1=s1.split(',')
print(l1)
l1=s1.split('-')
print(l1)

