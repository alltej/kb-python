
name = None

if not name:
    print("name = None::not None is True")
else:
    print("name = None::not None is False")

name = "John"

if not name:
    print("name = ", name, "::not None is True")
else:
    print("name = ", name, "::not None is False")

if None:
    print("None is True")
else:
    print("None is False")
