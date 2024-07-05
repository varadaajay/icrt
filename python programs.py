# multiplication
#  n=int(input("enter a number:"))
#  x=1
#  while x<=:
#      print(n,"*",x,"=",n*x)
#      x=x+1
# factors
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i=i+1
#prime number
# n=int(input("enter a any number:"))
# i=1
# c=0
# while i<=n:
#     if n%i==0:
#         c=c+1
#     i=i+1
# if c==2:
#     print("its a prime number")
# else:
#     print("its not a prime number")
# x=2
# y=2
# i=x
# while i<=x*y:
#     if i%x==0 and i%y==0:
#         print('lcm',i)
#         break
#     i=i+1
n=int(input("enter a number:"))
i=1
while i<=10:
    print(n,'*',i,"=",n*i)
    i=i+1
n=int(input("enter a number:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1
n=int(input("enter a number:"))
i=1
c=0
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print("it is a prime number")
else:
    print("it is not a prime number")
x=2
y=3
i=x
while i<=x*y:
    if i%x==0 and i%y==0:
        print('lcm',i)
    i=i+1