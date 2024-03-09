def input_matrix(rows_p, cols_p, matrix_p):
    print("Enter the elements of the matrix")
    for i in range(rows_p):
        for j in range(cols_p):
            matrix_p[i][j] = int(input(f"Enter element at [{i}][{j}]: "))


def add_matrix():
    pass


def display_matrix():
    pass


matrix = [[], [], []]

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

input_matrix(rows, cols, matrix)
