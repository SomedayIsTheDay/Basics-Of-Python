list_with_cubes = []
all_sum = 0
for i in range(1, 1000, 2):
    list_with_cubes.append(i**3)
for ind, val in enumerate(list_with_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_with_cubes[ind]
    list_with_cubes[ind] += 17
print(all_sum)
all_sum = 0
for ind, val in enumerate(list_with_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_with_cubes[ind]
print(all_sum)
