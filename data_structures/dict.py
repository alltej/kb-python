print("create a dictionary")
dict_1 = { 'a' : 'foo', 'b' : [0, 1, 2, 3] }
print(dict_1)
print()

print("access a dict's element by index 0(1)")
print(dict_1['b'])

print("Insert or set a dict's elements by index O(1):")
dict_1[5] = "bar"
print(dict_1)

print("Check if a dict contains a key O(1)")
is_exists = 5 in dict_1
print(is_exists)


print("Delete a value from a dict O(1):")
dict_2 = dict(dict_1)
del dict_2[5]
print(dict_2)
print(dict_1)

print("Remove and return an element from a specified index O(1):")
value = dict_2.pop('b')
print(value)
print(dict_2)

print("Get or pop can be called with a default value if the key is not found. \nBy default, get() will return None and pop() will throw an exception if the key is not found.")
value = dict_1.get('z', 0)
print(value)

print("Get the list of keys in no particular order (although keys() outputs the keys in the same order). In Python 3, keys() returns an iterator instead of a list.")
print(dict_1.keys())


print("Get the list of values in no particular order (although values() outputs the keys in the same order). In Python 3, keys() returns an iterator instead of a list.")
print(dict_1.values())

print("Iterate through a dictionary's keys and values:")
for key, value in dict_1.items():
    print(key, value)


print("Merge one dict into another:")
dict_1.update({'e' : 'elephant', 'f' : 'fish'})
print(dict_1)
