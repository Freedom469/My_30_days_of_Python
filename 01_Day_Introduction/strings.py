#!/bin/python3

#write strings on the python interactive shell. The strings are the following:
   # Your name
   # Your family name
   # Your country
   # I am enjoying 30 days of python

name = input("Enter your name: ")
family_name = input("Enter Your family Name: ")
country = input("Enter Your Country: ")
st = "I am enjoying 30 days of python."
print("Hello! My name is {} {} from {} and {} ".format(name, family_name, country, st))
