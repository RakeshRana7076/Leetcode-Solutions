class Solution(object):
    def majorityElement(self, nums):
        arr={}
        for num in nums:
            arr[num]=arr.get(num,0)+1
            if arr[num]>len(nums)//2:
                return num
        