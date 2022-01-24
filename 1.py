class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ind = 0
        for i in nums:
            if target - i not in d:
                d[i] = ind
            else:
                return [d[target - i], ind]
            ind = ind + 1
        return [None, None]
