# int() - Convert a number or string to an integer,
# or return 0 if no arguments are given.
print(int(22.5)) # truncates decimal, doesnt round up
# print(int("Hii")) can't conv non numeric strngs

print(int("123")) # can conv numeric strngs
print(int(True)) # considers as 1
print(int((2+4j).real)) # drct complex not allowed, extract real
print(int(-2.5))
print(int()) # gives 0 as no args
