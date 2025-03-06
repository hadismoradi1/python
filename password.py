b='A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
c='0','1','2','3','4','5','6','7','8','9'
d='@','#','$'
a=input('enter your password')
if len (a)<8:
    print('حداقل 8 کاراکتر داشته باشد')
elif a not in b:
    print('حداقل يک حرف بزرگ داشته باشد')
elif a not in c:
    print('حداقل يک عدد داشته باشد')
elif a not in d:
    print('حداقل يک کاراکتر خاص داشته باشد')
else:
    print(a)
    
    
