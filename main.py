def gen_row(prev_row):
    current_row = [1]
    for i in range(1, len(prev_row)):
        current_row.append(prev_row[i-1] + prev_row[i])
    current_row.append(1)
    return current_row


def gen_triangle(rows):
    triangle = [[1]]
    for i in range(rows):
        triangle.append(gen_row(triangle[-1]))
    return triangle


def row_str(row, num_width, space_width):
    row_str = ""
    for num in row:
        row_str += f"{num:{num_width}}".center(space_width)
    return row_str


def print_triangle(triangle):
    max_num_width = len(str(max(max(triangle, key=max))))
    space_width = max_num_width + 2  # Add space between numbers

    last_row_len = len(triangle[-1]) * space_width - (space_width - max_num_width) // 2

    for row in triangle:
        row_string = row_str(row, max_num_width, space_width)
        print(row_string.center(last_row_len))



exit_prog = False
gen_new = 'y'
while not exit_prog:
    completed = False
    if gen_new.lower().strip() == "y":
        triangle_len = input("Enter the number of rows to generate: ")
        valid_len = False
        while not valid_len:
            try:
                len_int = int(triangle_len)
                valid_len = True
            except ValueError as ve:
                triangle_len = input("Please enter a valid integer number of rows: ")
            
        user_triangle = gen_triangle(len_int)
        print_triangle(user_triangle)
        completed = True
    elif gen_new.lower().strip() == "n":
        exit_prog = True
        break
    else:
        gen_new = input("Please enter 'y' or 'n':")

    if completed:
        gen_new = input("Generate a new triangle (Y/N)?")