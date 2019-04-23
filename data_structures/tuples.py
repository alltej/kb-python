
##TUPLES - A tuple is a one dimensional, fixed-length, immutable sequence.
tup = (1, 2, 3)
print(tup)

#convert to tuple
list_1 = [1,2,3]
tup_1 = type(tuple(list_1))


#create a nested tuple

nested_tup = ([1,2,3],(4,5))
print(nested_tup)

print(nested_tup[0])

# Although tuples are immutable, their contents can contain mutable objects.
print("Modify a tuple's contents:")
nested_tup[0].append(4)
print(nested_tup[0])
print()

print("Concatenate tuples by creating a new tuple and copying objects:")
print((1, 3, 2) + (4, 5, 6))
print()


print("unpack tuples")

a, b = nested_tup
print(a, b)
print()


print("A common use of variable unpacking is when iterating over sequences of tuples or lists:")
seq = [( 1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(a, b, c)