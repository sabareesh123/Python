alp=input()
v=['a','e','i','o','u']
if alp.isalpha():
  if alp in v:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
