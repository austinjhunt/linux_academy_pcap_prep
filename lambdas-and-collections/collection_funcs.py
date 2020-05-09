#!/Users/huntaj/dev/pythoncertification/venv/bin/python3.7
from functools import reduce
# Higher order functions.
# Let's first look at "map".

# Remember algebra...
# f(x) = 1 + x
# Domain: [1, 2]
# Range: [2, 3]

# So we are just mapping a function over a collection

domain = [1, 2, 3, 4, 5]
# f(x) = x * 2
our_range = map(lambda num: num * 2, domain)

# our_range is a map object, so convert to a list
print(our_range)
print(list(our_range))


# Next, let's look at filter

evens = filter(lambda num: num % 2 == 0, domain)
print(evens)
print(list(evens))


# Reduce!
# So reduce is not a built in function yet, has to imported from functools
# Iterate over an iterable, and each time you modify an accumulator
the_sum = reduce(lambda acc, num: acc + num, domain, 0) # 0 is accumulator
print(the_sum) # this can be printed directly, because you're getting the final accumulator value.

words = ['Boss', 'a','Alfred','fig','Daemon','dig']
print("Sorting by default with sorted(words)")
print(sorted(words))

print("Sorting with a lambda key with sorted(words,key=lambda s: s.lower())")
# sort strings regardless of capitalization
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
print(words.sort()) # Modifies list, doesn't return a method.
print(words)
# ['Alfred', 'Boss', 'Daemon', 'a', 'dig', 'fig']

words.sort(key=str.lower)
print(words) # Passing a function as an argument requires that you do
# not use (), because you want to pass the function as an object, you dont want to call it.
# The str.lower works because of the following truth:
assert("my_string".lower() == str.lower("my_string"))

words.sort(key=str.lower, reverse=True)
print(words)