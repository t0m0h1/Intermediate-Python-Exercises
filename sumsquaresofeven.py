from typing import List

def sum_of_squares_of_evens(numbers: List[int]) -> int:
    total_sum = 0
    for num in numbers:
        if num % 2 == 0:
            total_sum += num * num
    return total_sum

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    calc = sum_of_squares_of_evens(numbers)
    print(calc)  # Output should be 56
