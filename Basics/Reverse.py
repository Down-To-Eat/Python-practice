n = int (input("enter the number"))
m,num,sum,a = len (str (n))-1,n,0,1
while n > 0:
    sum += (n%10**a)*(10**m)
    m -= 1
    a += 1
    n //= n
print ("the reverse of number",num,'is',sum)