n = int(input("Enter a number:"))

count = 0

while n>0:
    count+=1
    n=n//10

print(count)


# TC = O(log10(n))
# SC = O(1)