from typing import List

def insertion_sort(A: List[int]) -> List:
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
    
# driver code
if __name__ == '__main__':
    print(insertion_sort([5, 2, 4, 6, 1, 3])) # [1, 2, 3, 4, 5, 6]  
    print(insertion_sort([31, 41, 59, 26, 41, 58])) # [26, 31, 41, 41, 58, 59]


# Time complexity: O(n^2) which is 
# Space complexity: O(1)



