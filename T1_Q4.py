# A program to generate passwords

import random

print('''
Password Generator
==================
''')

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

number = input("number of passwords?")
number = int(number)

length = input("password length?")
length = int(length)

print("\nHere are your passwords:")

for pwd in range(number):
  password = ""
  for c in range(length):
    password += random.choice(chars)
  print(password)

print("\nEnjoy...Thank you")