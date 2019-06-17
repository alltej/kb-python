
msg = "hello" if True else "kamusta"

print(msg)

name=None
msg_2 = "John" if name else "Pete"
print(msg_2)

msg_2 = "John" if not name else "Pete"
print(msg_2)
