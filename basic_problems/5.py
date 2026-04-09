def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

num = int(input("enter a number:"))
print(factorial(num))     