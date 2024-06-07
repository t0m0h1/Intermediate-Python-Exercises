def longest_substring(s: str) -> int:
    l = 0
    longest = 0
    set1 = set()
    n = len(s)
    
    for r in range(n):
        while s[r] in set1:
            set1.remove(s[l])
            l += 1
        set1.add(s[r])
        longest = max(longest, r - l + 1)

    return longest


def shortest_substring(s: str) -> int:
    l = 0
    shortest = float('inf')
    set1 = set()
    n = len(s)
    
    for r in range(n):
        while s[r] in set1:
            set1.remove(s[l])
            l += 1
        set1.add(s[r])
        if len(set1) == 3:
            shortest = min(shortest, r - l + 1)

    return shortest


# driver code
if __name__ == '__main__':
    print(longest_substring("abcabcbb")) # 3
    print(longest_substring("bbbbb")) # 1
    print(longest_substring("abcdefghijklmnopqrstwxyz")) # 26
    print(shortest_substring("abcabcbb")) # 3