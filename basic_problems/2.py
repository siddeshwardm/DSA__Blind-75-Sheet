n= int(input("Enter the number:"))
num = n
result = 0

while n>0:
    ld = n%10
    result = (result*10) +ld
    n= n//10

if(result == num):
    print("palindrome")
else:
    print("not a palindrome")


# TC = O(log10(n))
# SC = O(1)
