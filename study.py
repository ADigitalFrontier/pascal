# This program studies the digital roots of the center "column" of Pascal's triangle, i.e: [1, 2, 6, 20, 70, 252, 924, etc..]. From a simple hand-written observation it seems that the digital root of each center element is either 3, 6, or 9, or follows the following property: If the digital root of the element is not 9, then for each element of the left and on the right, add its digital root to the elements digital root, and continue left and right until a 3, 6, or 9 is reached. Do not add the 3, 6, or 9. This grouping of non-369 elements will yield a digital root of either 3 6 or 9. This program verifies my hand-written observations with thousands of programmatically generated examples which seems to indicate that this property likely holds for any number of rows. Additionally, it seems that this sequence converges to repeating 9s as it increases in length.


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


to_study = gen_triangle(3000)


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