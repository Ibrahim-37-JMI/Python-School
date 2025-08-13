#wap to differenciate btw break and continue

print ("the loop with 'break' produces output as : ")

for i in range (1,11):
    if i % 3==0:
        break
    else:
        print(i)

print ("the loop with 'continue' produces output as : ")

for i in range (1,11):
    if i % 3==0:
        continue
    else:
        print(i)
