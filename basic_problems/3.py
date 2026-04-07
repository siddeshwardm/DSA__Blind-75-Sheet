n = int(input("enter the number:"))
total = 0
num = n
nod = len(str(n))


while num>0:
    ld = num%10
    total = total + (ld**nod)
    num = num//10

print(total == n)