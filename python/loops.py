"""
Topic: For Loop
"""

fruits = ["Apple", "Banana", "Pear", "Watermelon", "Orange"]

for fruit in fruits:
	print(fruit)

"""
With For Loop we can iterate over a list
and use each value in various ways
"""


"""
Topic: Continue and Break
Altering the Iterations
"""

numbers = [1, 2, 3, 4, 7]
for number in numbers:
	if (number == 2 or number == 4): continue
	if (number == 7): break
	print(number)