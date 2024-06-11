from typing import List
import random
import timeit

def insertion_sort(A: List[int]) -> List[int]:
    n = len(A)
    i = 1
    while i < n:
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current
        i += 1
    return A
    
numbers = [random.randint(0, 2000) for _ in range(2000)]

def rounded():
    return round(timeit.timeit(lambda: insertion_sort(numbers), number=1), 4)

if __name__ == '__main__':
    print(insertion_sort([5, 2, 4, 6, 1, 3]))
    print(rounded())

# time complexity: O(n^2)
# space complexity: O(1)
