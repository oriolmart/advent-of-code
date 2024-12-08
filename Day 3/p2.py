import re

file = open("input.txt", "r")

text: str = ""

for line in file:
    text += line

text = text.strip()

matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", text)

result: int = 0
enabled: bool = True

for match in matches:
    if match[2] == "" and enabled:
        result += int(match[0]) * int(match[1])
    else:
        if match[2] == "do()":
            enabled = True
        else:
            enabled = False

print(result)