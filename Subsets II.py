class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(index, arr):
            if index == len(nums):
                res.append(arr[::])
                return
            
            #include nums[index]
            arr.append(nums[index])
            backtrack(index+1,arr)
            arr.pop()

            #not include nums[index]
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            backtrack(index+1,arr)

        backtrack(0,[])
        return res
