import random

# read file
with open('area.txt', 'r', encoding='utf-8') as file:
    result = file.readlines()
result = [x.strip() for x in result]
length = len(result) - 1
position = random.randint(0, length)
