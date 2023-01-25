n=int(input("enter a number"))
num=n
sum=0
while(n>0):
    a=n%10
    sum=sum*10+a
    n=n//10
if(sum==num):
    print("the given number is palindrom")
else:
    print("the given number is not a palindrom")
