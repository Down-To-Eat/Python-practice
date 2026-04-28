n = int (input ("enter the number"))
num = n
f = 1
while n > 0:
    f *= n
    n -= 1
print ("The factorial of",num,'is',f)