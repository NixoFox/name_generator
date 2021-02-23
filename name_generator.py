#!/bin/python3
from random import randint

female_names = "female_names.txt"
male_names = "male_names.txt"
last_names = "last_names.txt"
all_names = ""
is_last = ""
gender = ""
result = ""

def get_gender():
  global gender
  gender = input("[b]oth, [f]emale, [m]ale: ")
  if not(gender == "b" or gender == "f" or gender == "m"):
    print("error: invalid value")
    get_gender()
get_gender()

def get_is_last():
  global is_last
  is_last = input("include last name [1, 0]: ")
  try:
    is_last = bool(is_last)
  except:
    print("error: invalid value")
    get_is_last()
get_is_last()

if gender == "b":
  with open(female_names, "r") as f:
    for i in f.readlines():
      all_names += i
  with open(male_names, "r") as f:
    for i in f.readlines():
      all_names += i
  all_names = all_names.split()
elif gender == "f":
  with open(female_names, "r") as f:
    all_names = f.readlines()
elif gender == "m":
  with open(male_names, "r") as f:
    all_names = f.readlines()

result = all_names[randint(0, len(all_names))]
result = result[:-2]

if is_last == True:
  last_names_lines = ""
  with open(last_names, "r") as f:
    last_names_lines = f.readlines()
  result += " " + last_names_lines[randint(0, len(last_names))]
  result = result[:-2]

print(result)

