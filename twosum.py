class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                return [i, j] if self.nums[i] + self.nums[j] == self.target else 'No two sum solution'
    

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    search = Solution(nums, target)
    print(search.twoSum())