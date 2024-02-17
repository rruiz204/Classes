"""
Topic: Conditions
"""

edad = 17
if (edad < 13):
	print("You are a child nigga")
elif (edad > 13 and edad < 19):
	print("You are a pubert man")
else:
	print("Does your back hurts?")

"""
The result of the above code depends on 'edad'
"""


"""
Topic: Logic Operators
"""

num_a = 1
num_b = 2
num_c = 3
expression_a = num_b % 2 == 0

# AND
if (num_a < num_c and num_b < num_c and expression_a):
	print("All expressions are True")
else:
	print("Some expression is not True")


# OR
if (num_a > num_c or expression_a):
	print("Some expression is True")
else:
	print("No expression is True")