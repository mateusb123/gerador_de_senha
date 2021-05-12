import string
import sys
from random import random, choice

arg = sys.argv[::1]

values = string.ascii_letters + string.digits
l = arg[1]
password = ""

for c in range(l):
  password += choice(values)
  
print(f'password: {password}')
