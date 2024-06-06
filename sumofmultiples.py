def sum_of_multiples(n: int, m: int) -> int:
    multiples = [i for i in range(m, n, m)]
    print(multiples)  
    return sum(multiples)

if __name__ == "__main__":
    n = 10
    m = 3
    result = sum_of_multiples(n, m)
    print(result)

