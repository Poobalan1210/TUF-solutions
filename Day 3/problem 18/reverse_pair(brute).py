class solution:
    def reverse_pair(self,nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]*2:
                    count+=1

        return count





if __name__ =="__main__":
    soln=solution()
    print(soln.reverse_pair([2,4,3,5,1]))