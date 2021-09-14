from time import perf_counter_ns

# head-on
start_1 = perf_counter_ns()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = [i for i in src if src.count(i) == 1]
finish_1 = perf_counter_ns()
print(unique_src, finish_1 - start_1)

# optimized (but head-on was shorter)
start_2 = perf_counter_ns()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]  # need more numbers to be more optimized then head-on
unique_src = set()
each = set()
for i in src:
    if i not in each:
        unique_src.add(i)
    else:
        unique_src.discard(i)
    each.add(i)
unique_src_sort = [el for el in src if el in unique_src]
finish_2 = perf_counter_ns()
print(unique_src_sort, finish_2 - start_2)
