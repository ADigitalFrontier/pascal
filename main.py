from pascal import gen_triangle, print_triangle

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