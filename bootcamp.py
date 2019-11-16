#!/usr/bin/env python
numbers = []
size = int(input("How many numbers so you want to input:\n"))
pro_even = []
sum_odd = []
#Read a list of integers from user input.
for i in range(size):
    element = int(input("Enter integer:\n"))
    numbers.append(element)
#Find all pairs of numbers in the list whose product is even and whose sum is odd
for item1 in numbers:
    for item2 in numbers:
        if (item1*item2) % 2 == 0:
            pro_even.append((item1,item2))
        if (item1 + item2) % 2 != 0:
            sum_odd.append((item1,item2))
#Print out a formatted list of the pairs
print("Pairs with even product\n")
print("{}".format(pro_even))
print("Pairs with odd sum\n")
print("{}".format(sum_odd))
