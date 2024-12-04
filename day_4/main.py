import re

'''
    UTILS:
    return the diagonal elements of a matrix
'''
def extract_diagonals(matrix: list[list[str]], n: int, m: int, reverse=False) -> list[str]:
    diagonals = []
    # Top-right (or top-left if reverse=True)
    for start_col in range(m):
        diagonal = ""
        row, col = 0, start_col
        while 0 <= row < n and 0 <= col < m:
            diagonal += matrix[row][col]
            row += 1
            col += -1 if reverse else 1
        diagonals.append(diagonal)

    # Bottom-right (or bottom-left if reverse=True)
    for start_row in range(1, n):
        diagonal = ""
        row, col = start_row, m - 1 if reverse else 0
        while 0 <= row < n and 0 <= col < m:
            diagonal += matrix[row][col]
            row += 1
            col += -1 if reverse else 1
        diagonals.append(diagonal)

    return diagonals


'''
    UTILS:
    check if a 3x3 matrix contains the cross "MAS"-"MAS"
'''
def is_correct_x_mas(matrix: list[list[str]]) -> bool:    
    if (matrix[0][0] == "M" and matrix[1][1] == "A" and matrix[2][2] == "S" and matrix[0][2] == "M" and matrix[2][0] == "S"):
        return True

    # Check all the possible rotations of the matrix
    for _ in range(3):
        matrix = list(zip(*matrix[::-1]))
        if (matrix[0][0] == "M" and matrix[1][1] == "A" and matrix[2][2] == "S" and matrix[0][2] == "M" and matrix[2][0] == "S"):
            return True

    return False


'''
    PART 1:
    Given a matrix of characters, find the number of occurrences of the word "XMAS" in all possibile pattern in the matrix.
'''
def get_xmas_occurrences(data: str) -> int:
    xmas_occurrences: int = 0
    pattern = r"XMAS"

    # Create a matrix from input data
    lines = data.split("\n")
    matrix = [list(line) for line in lines]
    n, m = len(matrix), len(matrix[0])

    # Horizontal occurrences
    for line in lines:
        xmas_occurrences += len(re.findall(pattern, line))
        xmas_occurrences += len(re.findall(pattern, line[::-1]))

    # Vertical occurrences
    for col in range(m):
        column = "".join(matrix[row][col] for row in range(n))
        xmas_occurrences += len(re.findall(pattern, column))
        xmas_occurrences += len(re.findall(pattern, column[::-1]))
   
    # Diagonal occurrences (both directions)
    diagonals = extract_diagonals(matrix, n, m, reverse=False)
    reversed_diagonals = extract_diagonals(matrix, n, m, reverse=True)

    for diagonal in diagonals + reversed_diagonals:
        xmas_occurrences += len(re.findall(pattern, diagonal))
        xmas_occurrences += len(re.findall(pattern, diagonal[::-1]))

    return xmas_occurrences


'''
    PART 2:
    Given a matrix of characters, find the number of cross of the word "MAS" in all possibile pattern in the matrix.
'''
def get_mas_crosses(data: str) -> int:
    mas_occurrences: int = 0

    # Create a matrix from input data
    lines = data.split("\n")
    matrix = [list(line) for line in lines]
    n, m = len(matrix), len(matrix[0])

    # divide the matrix in all the possible 3x3 sub-matrices
    sub_matrices = []
    for row in range(n - 2):
        for col in range(m - 2):
            sub_matrix = [matrix[row + i][col:col + 3] for i in range(3)]
            sub_matrices.append(sub_matrix)

    # Check if the sub-matrix contains the cross "MAS"-"MAS"
    for sub_matrix in sub_matrices:
        if is_correct_x_mas(sub_matrix):
            mas_occurrences += 1

    return mas_occurrences


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()

    print(get_xmas_occurrences(data))
    print(get_mas_crosses(data))