i=-1
a=int(input("enter a value:"))
t=int(input("enter till how much:"))
while i<t:
    i=i+1
    print(a,'x',i,'=',i*a)
print(a)
print("----------------------------------------------------------------------------------------------")
a=int(input("enter a value:"))
n=int(input("till how much number do you want it to run:"))
n+=1
for i in range(0,n,1):
    print(a,"x",i,'=',a*i)
print("------------------------------------------------------------------------------------------------")
a=input("enter the symbol:")
b=int(input("how many times do you want the symbol to reapeat:"))
i=0
for i in range (1,b,1):
    i=i+1 
    print(a*i)
print("_______________________________")
n=[10,9,8,7,6,5,4,3,2,1,0]
n.pop(5)
print(n)
print("__________error handling_____________________")
a=int(input("enter a value"))
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("try and except are end")
print("________________________________how many error____________________________")
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

    

