file = open("input.txt", "r")

matrix: list[str] = []
xmas_count: int = 0

for line in file:
    matrix.append(line)



for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "X":
            if not (row - 3 < 0) and matrix[row - 1][col] == "M" and matrix[row - 2][col] == "A" and matrix[row - 3][col] == "S": xmas_count += 1
            if not (row - 3 < 0) and not (col + 3 > len(matrix[row])) and matrix[row - 1][col + 1] == "M" and matrix[row - 2][col + 2] == "A" and matrix[row - 3][col + 3] == "S": xmas_count += 1
            if not (col + 3 > len(matrix[row])) and matrix[row][col + 1] == "M" and matrix[row][col + 2] == "A" and matrix[row][col + 3] == "S": xmas_count += 1
            if not (row + 3 > len(matrix) - 1) and not (col + 3 > len(matrix[row])) and matrix[row + 1][col + 1] == "M" and matrix[row + 2][col + 2] == "A" and matrix[row + 3][col + 3] == "S": xmas_count += 1
            if not (row + 3 > len(matrix) - 1) and matrix[row + 1][col] == "M" and matrix[row + 2][col] == "A" and matrix[row + 3][col] == "S": xmas_count += 1
            if not (row + 3 > len(matrix) - 1) and not (col - 3 < 0) and matrix[row + 1][col - 1] == "M" and matrix[row + 2][col - 2] == "A" and matrix[row + 3][col - 3] == "S": xmas_count += 1
            if not (col - 3 < 0) and matrix[row][col - 1] == "M" and matrix[row][col - 2] == "A" and matrix[row][col - 3] == "S": xmas_count += 1
            if not (row - 3 < 0) and not (col - 3 < 0) and matrix[row - 1][col - 1] == "M" and matrix[row - 2][col - 2] == "A" and matrix[row - 3][col - 3] == "S": xmas_count += 1

print(xmas_count)
