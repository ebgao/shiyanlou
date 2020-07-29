#!/usr/bin/env python3
i = 0
sum = 0
while i < 10:
    i += 1
    a=float(input("Please input a number:"))
    sum = sum + a

average = sum / i
print("count = ", i)
print("sum = ", sum)
print("Average = {:.3f}".format(average))

