
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
   var = var -1
   try:
       if var == 5:
          continue
       print('Current variable value :', var)
   finally:
       print('finally here: ', var)

print("Good bye!")
