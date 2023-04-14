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


to_study = gen_triangle(100)


center_elems = []
for i, row in enumerate(to_study):
    if i % 2 == 0:
        center_elem = int(len(row)/2)
        center_elems.append(row[center_elem])



center_droots = []
for celem in center_elems:
    center_droots.append(digital_root(celem))

print(center_droots)

