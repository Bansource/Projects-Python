"""n = 12359     sum = 0

    n      r = n % 10     n= n//10      sum = sum + r
   12359        9           1235        9 + 0
   1235         5           123         14 = 9 + 5
   123          3           12
   12           2           1
   1            1           0                   """

# in this challenge if n = 12359
# 1 + 2 + 3 + 5 + 9 = 20

n = int(input())
total = 0

while n > 0:
    r = n % 10
    total = total + r
    n = n // 10

print(f"The sum of digits is {total}")