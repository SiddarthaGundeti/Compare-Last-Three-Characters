a=input()
b=input()
length1=len(a)
length2=len(b)
a=a[length1-3:]
b=b[length2-3:]
result=a==b
print(result)
