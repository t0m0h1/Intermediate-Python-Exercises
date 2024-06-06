def greatest_common_divisor(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

def lowest_common_multiple(n1, n2):
    return n1 * n2 // greatest_common_divisor(n1, n2)


if __name__ == '__main__':
    print(greatest_common_divisor(12, 18)) # 6
    print(lowest_common_multiple(12, 18)) # 36
