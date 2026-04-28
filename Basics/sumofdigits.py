n = int (input("enter a number"))
num = n
sum = 0
while n >0:
    sum += n%10
    n //= 10
print ("the sum of digits of number",num,'is',sum)
