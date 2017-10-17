#!usr/bin/python3

# Project Euler
# Problem 22: Names Scores

import string

with open("names.txt", "r") as f:
    names = f.readlines()

names = names[0].split(",") #

for idx in range(len(names)):
    names[idx] = names[idx].replace('"', '')
names = sorted(names)

def count_name_score(name, idx):
    score = 0
    for letter in name:
        score += string.lowercase.index(letter.lower()) + 1
    score = score * (idx + 1)
    return score

count = 0
for idx, name in enumerate(names):
    count += count_name_score(name, idx)
print(count)
