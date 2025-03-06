list1=[]
a=int(input('enter number1:'))
b=int(input('enter number2:'))
c=input('odd or even')
if a>b:
    if c=='even':
        for h in range(a,b):
            if h%2==0:
                list1.append(h)
        print(list1)
    elif c=='odd':
        for h in range(a,b):
            if h%2!=0:
                list1.append(h)
        print(list1)
    else:
        print('wrong')
elif b>a:
    if c=='even':
        for h in range(a,b):
            if h%2==0:
                list1.append(h)
        print(list1)
    elif c=='odd':
        for h in range(a,b):
            if h%2!=0:
                list1.append(h)
        print(list1)
    else:
        print('wrong')
    
    
