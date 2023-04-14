# Author: Aaron Stone
# Created: 4/14/2023
# 
# This program provides various functions for generating and displaying Pascal's triangles.


def gen_row(prev_row):
    current_row = [1]
    for i in range(1, len(prev_row)):
        current_row.append(prev_row[i-1] + prev_row[i])
    current_row.append(1)
    return current_row


def gen_triangle(rows):
    triangle = [[1]]
    for i in range(rows-1):
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