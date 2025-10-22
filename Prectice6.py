# find largest number in 4 numbers

a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))
d = int(input("Fourth Number: "))

if(a>b and a>c and a>d):
    print("The largest value is ",a)
if(b>c and b>d and b>a):
    print("The largest value is ",b)
if(c>a and c>b and c>d):
    print("The largest value is ",c)
else:
    print("The largest value is ",d)

