def greatest_common_divisor(n1, n2):
    divisors = []
    for i in range(1, n1):
        for j in range(1, n2):
            common_d = i % j == 0
            divisors.append(common_d)





def lowest_common_multiple(n1, n2):
    pass