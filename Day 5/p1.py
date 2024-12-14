file = open("input.txt", "r")

order_list: list[list[int]] = []

updates_input: bool = False

for line in file:
    if line.strip() == "":
        updates_input = True
    elif updates_input:
        print(line.strip())
    else:
        

print(order_list)
