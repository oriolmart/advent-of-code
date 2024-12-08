
# Inicializar listas para cada columna
left_column: list[int] = []
right_column: list[int] = []

file = open("input.txt", "r")

for line in file:
    numbers: list[str] = line.split()
    left_column.append(int(numbers[0]))
    right_column.append(int(numbers[1]))

similarity_score: int = 0

for i in range(len(left_column)):
    for j in range(len(right_column)):
        if left_column[i] == right_column[j]:
            similarity_score += left_column[i]

print(similarity_score)
