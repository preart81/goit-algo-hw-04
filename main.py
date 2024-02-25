import timeit
import random

from sort_algs import bubble_sort
from sort_algs import insertion_sort
from sort_algs import merge_sort
from sort_algs import quick_sort
from sort_algs import radix_sort
from sort_algs import selection_sort
from sort_algs import shell_sort


if __name__ == "__main__":
    S, M, L = 100, 1_000, 10_000
    arr_small = [random.randint(1, 1_000) for _ in range(S)]
    arr_medium = [random.randint(1, 10_000) for _ in range(M)]
    arr_large = [random.randint(1, 100_000) for _ in range(L)]

N = 1
ts_insertion_sort = timeit.timeit(lambda: insertion_sort(arr_small), number=N)
ts_merge_sort = timeit.timeit(lambda: merge_sort(arr_small), number=N)
ts_sorted = timeit.timeit(lambda: sorted(arr_small), number=N)

tm_insertion_sort = timeit.timeit(lambda: insertion_sort(arr_medium), number=N)
tm_merge_sort = timeit.timeit(lambda: merge_sort(arr_medium), number=N)
tm_sorted = timeit.timeit(lambda: sorted(arr_medium), number=N)

tl_insertion_sort = timeit.timeit(lambda: insertion_sort(arr_large), number=N)
tl_merge_sort = timeit.timeit(lambda: merge_sort(arr_large), number=N)
tl_sorted = timeit.timeit(lambda: sorted(arr_large), number=N)


print(f"+{'-' * 22}+{'-' * 19}+{'-' * 19}+{'-' * 19}+")
print(f"| {'Алгоритм':<20} | {S:7} елементів | {M:7} елементів | {L:7} елементів |")
print(f"+{'-' * 22}+{'-' * 19}+{'-' * 19}+{'-' * 19}+")
print(
    f"| {'Insertion Sort':<20} | {ts_insertion_sort:17.6f} | {tm_insertion_sort:17.6f} | {tl_insertion_sort:17.6f} |"
)
print(
    f"| {'Merge Sort':<20} | {ts_merge_sort:17.6f} | {tm_merge_sort:17.6f} | {tl_merge_sort:17.6f} |"
)
print(
    f"| {'Timsort (Sorted)':<20} | {ts_sorted:17.6f} | {tm_sorted:17.6f} | {tl_sorted:17.6f} |"
)
print(f"+{'-' * 22}+{'-' * 19}+{'-' * 19}+{'-' * 19}+")
