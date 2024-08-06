a,b,c=map(int,input("enter value of three number:").split())
if a>b and a>c:print("a is big ")
elif b>a and b>c:print("b is big number")
elif c>a and c>b:
    print("c is big number")
elif a==b and b==c:
    print("given numbers are equal")
else:
    print("given two values are equal and great")
print(max(a,b,c))
print(max(a,b,c)+a,max(a,b,c)+b,max(a,b,c)+c)
print(a,b,c)
print("a+b=",a+b)
print("b+c=",b+c)



















