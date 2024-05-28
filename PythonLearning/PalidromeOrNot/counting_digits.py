"""n = 12359     r = n% 10 will give last num (9,5,3,2,1)   counter = 0

    n         n= n//10         counter = counter + 1
   12359        1235                1
   1235         123                 2
   123          12                  3
   12           1                   4
   1            0                   5"""

n = int(input())
counter = 0

while n > 0:
    n = n // 10
    counter = counter + 1
print(counter)


