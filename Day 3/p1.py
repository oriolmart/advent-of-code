import re

file = open("input.txt", "r")

text: str = ""

for line in file:
    text += line

text = text.strip()

matches = re.findall(r"mul\((\d+),(\d+)\)", text)

print(matches)

result: int = 0

for match in matches:
    result += int(match[0]) * int(match[1])

print(result)
