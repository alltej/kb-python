print("A set is an unordered sequence of unique elements.")
print()
print("create a set")

set_1 = set([0, 1, 2, 3, 4, 5])
print(set_1)

set_2 = {1, 2, 3, 5, 8, 13}
print(set_2)

print("Union of sets")
print(set_1 | set_2)


print()

print("Intersection of sets")
print(set_1 & set_2)
print()

print("Difference of sets")
print(set_1 - set_2)
print(set_2 - set_1)
print()

print("Symmetric difference")
print(set_1 ^ set_2)
print()

print("Subset")
set_3 = {1, 2,3}
print(set_3.issubset(set_2))
print()

print("Superset")
print(set_2.issuperset(set_3))
print()
print("Equal")
is_set_equal = {1,2,3} == {3,2,1}
print(is_set_equal)