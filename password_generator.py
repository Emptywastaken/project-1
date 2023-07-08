#2

import secrets
import string
from random import randint

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = randint(10, 17)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += secrets.choice(alphabet)

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)