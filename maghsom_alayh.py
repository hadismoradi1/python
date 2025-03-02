list1=[]
list2=[]
a=int(input('enter number1:'))
b=int(input('enter number2:'))
for h in range(1,a+1):
    if a%h==0:
        list1.append(a)
        print(h)
for g in range(1,a+1):
    if b%h==0:
        list2.append(b)
        print(h)
print(list1)
print(list2)
list1.sort()

