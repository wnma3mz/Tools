# coding: utf-8
import string
# print(string.ascii_uppercase)
str_ = "–·–· ––– –· ··–· · ··· ··· ·· ––– –·   ·· ···   – ···· ·· ··· ––– ···   ··   ·–·· ·· –·– ·   –·–– ––– ··– "
# str_ = "··–· ·–· ––– ··· –"
mosi_dict_1 = {}
mosi_dict_2 = {}

a_list = ["·–", "–···", "–·–·", "–··", "·", "··–·", "-–·", "····", "··", "·–––", "–·–", "·–··",
          "––", "–·", "–––", "·––·", "––·–", "·–·", "···", "–", "··–", "···–", "·––", "–··–", "–·––", "––··", ]

for char, value in zip(string.ascii_uppercase, a_list):
    mosi_dict_1[value] = char
    mosi_dict_2[char] = value
from pprint import pprint
# pprint(mosi_dict_1)
# pprint(mosi_dict_2)

for char in str_.split(" "):
    try:
        print(mosi_dict_1[char], end="")
    except:
        print(" ")
string = "I LOVE YOU"
for char in string:
    if char != " ":
        print(mosi_dict_2[char], end=" ")
