
# Inicializar listas para cada columna
left_column: list[int] = []
right_column: list[int] = []

file = open("input.txt", "r")

for line in file:
    numbers: list[str] = line.split()
    left_column.append(int(numbers[0]))
    right_column.append(int(numbers[1]))

left_column.sort()
right_column.sort()

total_distance: int = 0

for i in range(len(left_column)):
    difference = right_column[i] - left_column[i]
    distance = abs(difference)
    total_distance += distance

print(total_distance)
