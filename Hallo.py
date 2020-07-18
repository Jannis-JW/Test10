"""
##Euler 1
x = 1
y = 2
summe = 2
print(x)
print(y)
while y + x < 4000000:
    x += y
    if x%2== 0:
        summe += x
        print(x)
    y += x
    if y%2== 0:
        summe += y
        print(y)
print(summe)
"""
"""
## Euler 2
x = 600851475143
y = 2
while x > 1:
    if x%y == 0:
        print(y)
        x = x/y
    else:
        y+= 1
print(y)
"""

## Euler 3 incomplete
def isPal(num):
    numString = str(num)
    for i in range(0,len(numString) // 2+1):
        if (numString[i] != numString[-i - 1]):
            return False
    return True


max = 0

max1, max2 = 0, 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        pro = i * j
        if isPal(pro):
            if (pro > max):
                max = pro
                max1, max2 = i, j


print(str(max))
print(str(max) + ' = ' + str(max1) + ' * ' + str(max2))

"""
## Euler 4
x = 1
y = False
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while not y:
    if x%a1== 0 and x%a2== 0 and x%a3== 0 and x%a4== 0 and x%a5== 0 and x%a6== 0 and x%a7== 0 and x%a8== 0 and x%a9== 0 and x%a10== 0 and x%a11== 0 and x%a12== 0 and x%a13== 0 and x%a14== 0 and x%a15== 0 and x%a16== 0 and x%a17== 0 and x%a18== 0 and x%a19== 0:
         print(x)
         y = True
    else:
         x+= 1
"""
"""
## Euler 5
summe = 0
y = 0
x = 1
while x <= 100:
    summe += x**2
    print(summe)
    y += x
    x += 1
y = y**2
summe = y - summe
print(summe)
"""

##Euler 6
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) +1):
        if (num % i == 0):
            return False

    return True

count= 1
num = 2

while (count<10001):
    num += 1
    if isPrime(num):
        count +=1

print(str(num))

"""
##Euler 7
for i in range (1,1000):
    for o in range(1,1000):
        for p in range(1,1000):
            if (i+o+p == 1000) and i<o:
                if (i*i + o*o == p*p):
                    print(i)
                    a = i
                    print(o)
                    b = o
                    print(p)
                    c = p
                    Lösung = a * b * c
                    print(Lösung)
                    exit()
"""
"""
## Euler 8
import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False

    return True
sum = 0
for i in range(2,2000000):
    if isPrime(i):
        sum += i
print(str(sum))
"""
