#!/Users/huntaj/dev/pythoncertification/venv/bin/python3.7

# Lambda = single expression anonymous function
# So this function is one line, and it explicitly returns the value it is
# calculating, which means it can be converted to a lambda function.
def square(num):
    return num * num
square(2) # => 4

# Result of expression within lambda is always going to be returned.
# So the below lambda function is equivalent to the above def .. function
lambda num: num * num

# You can assign a lambda function to a variable.
square_lambda = lambda num: num * num

assert square_lambda(4) == square(4)

# Normal function, multiple lines/expressions
def name(a, b):
    print("Something")
    1 + a
    return b
