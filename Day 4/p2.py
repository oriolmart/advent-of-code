file = open("input.txt", "r")

matrix: list[str] = []
xmas_count: int = 0

for line in file:
    matrix.append(line)



for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            if row != 0 and row != len(matrix) - 1 and col != 0 and col != len(matrix[row]) - 1:
                up_left = matrix[row - 1][col - 1]
                up_right = matrix[row - 1][col + 1]
                down_left = matrix[row + 1][col - 1]
                down_right = matrix[row + 1][col + 1]
                if (up_left == "M" and down_right == "S") or (up_left == "S" and down_right == "M"): 
                    if (up_right == "M" and down_left == "S") or (up_right == "S" and down_left == "M"):
                        xmas_count += 1

print(xmas_count)
