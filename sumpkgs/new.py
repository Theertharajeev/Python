from mypkg.Calculations import module1
from mypkg.Calculations import module2
from mypkg.Calculations import module3

m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
s=module1.sum(m,n)
print("sum",s)
a=module2.avg(m,n)
print("average",a)
p1=module3.power(m)
print("power of ",m
