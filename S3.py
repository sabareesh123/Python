ab=input()
r=["a","e","i","o","u","A","E","I","O","U"]
if((ab>='a' and ab<='z') or (ab>='A' and ab<='Z')):
  if ab in r:
     print("Vowel")
  else:
     print("Consonant")
else:
   print("invalid")
