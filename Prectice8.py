# print "palindrome or not"

list = [3,4,4556,1]

list1 = list.copy()
list1.reverse()

if(list1 == list):
    print("Palindrome")
else:
    print("Not Palindrome")