#!/usr/bin/env python3
amount = float(input("Enter amount: "))  # enter money
inrate = float(input("Enter Interest rate: "))  # enter lilv
period = int(input("Enter period: "))  # enter peried
value = 0
year = 1
while year <= period:
        value = amount + (inrate * amount)
        print("Year {} Rs. {:.2f}".format(year, value))
        amount = value
        year = year + 1
