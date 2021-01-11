
class Solution:
    def findDuplicate(self,nums):
        fast=nums[0]
        slow=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        fast=nums[0]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]
        return fast
                         


if __name__ =="__main__":
    nums=[1,5,3,2,4,1,9]
    soln=Solution()
    print(soln.findDuplicate(nums))