class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
    
       nums3=nums1+nums2
       nums3.sort()
       x=len(nums3)
       if x%2 !=0:
          return float(nums3[int(x/2)])
 
       return float((nums3[int((x-1)/2)] + nums3[int(x/2)])/2.0)
solution=Solution()