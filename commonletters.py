from time import time
import timeit

class Solution:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def find_common(self):
        common = [letter for letter in self.str1 if letter in self.str2]
        return common if common else 'No common letters found'
    


if __name__ == '__main__':
    str1 = 'string'
    str2 = 'string'
    search = Solution(str1, str2)
    print(search.find_common())
    print(f'{round(timeit.timeit("search.find_common()", globals=globals(), number=1000000), 3)} seconds')