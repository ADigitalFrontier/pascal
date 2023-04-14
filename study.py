# Author: Aaron Stone
# Created: 4/14/2023
# 
# This program studies the sequence defined in README.md


# Modify this variable to set the number of rows you wish to consider when generating the sequence
ROWS_TO_STUDY = 100


from pascal import gen_triangle


def digital_root(num):
    numstr = str(num)
    numlen = len(numstr)
    numsum = 0
    for i in range(numlen):
        numsum += int(numstr[i])
    if len(str(numsum)) > 1:
        return digital_root(numsum)
    else:
        return numsum


def get_partition(arr, start, end):
    return arr[start:end]


to_study = gen_triangle(ROWS_TO_STUDY)


center_elems = []
for i, row in enumerate(to_study):
    if i % 2 == 0:
        center_elem = int(len(row)/2)
        center_elems.append(row[center_elem])


center_droots = []
for celem in center_elems:
    center_droots.append(digital_root(celem))


integer_sequence = []


last_start = 0
for cur_index, num in enumerate(center_droots):
    if num == 3 or num == 6 or num == 9:
        partition = get_partition(center_droots, last_start, cur_index)
        if len(partition) > 0:
            dr = digital_root(sum(partition))
            integer_sequence.append(dr)
            # print("P: " + str(dr))
        # print(num)
        integer_sequence.append(num)
        last_start = cur_index+1
partition = get_partition(center_droots, last_start, len(center_droots))
if len(partition) > 0:
    dr = digital_root(sum(partition))
    integer_sequence.append(dr)
    # print("P: " + str(dr))

print(integer_sequence)