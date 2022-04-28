from det import det

def to_row(vector: str) -> list[int | float]:
    row_str = vector.split(' ')
    row_float = []
    for num in row_str:
        if '.' in num:
            row_float.append(float(num))
        else:
            row_float.append(int(num))
    return row_float


def safe_input(message: str) -> list[int | float]:
    """Catches invalid input to return a list of numbers"""
    while True:
        try:
            return to_row(input(message).strip(' '))
        except ValueError:
            print("Numbers only, please.")


print("Welcome to determinant calculator.\nEnter first row, separated by spaces, e.g. 3 1 2")
matrix = [safe_input('')]
n = len(matrix[0])

for _ in range(n - 1):
    # for row in matrix:
    #     print(row)

    new_row = safe_input('Next row:\n')
    while len(new_row) != n:
        print(f"Invalid length; should be {n}.")
        new_row = safe_input('Next row:\n')
    matrix.append(new_row)

print("\n\nMatrix:")
for row in matrix:
    print(row)
print(f"Determinant is {det(matrix)}.")
