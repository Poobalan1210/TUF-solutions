class solution:
    def majority_element(self,nums):
        count=0
        element=0
        for no in nums:    #moore algorithm only if one no is greater the n/2
            if count == 0:
                element = no
            if no == element:
                count+=1
            else:
                count-=1
        return element

if __name__ =="__main__":
    soln=solution()
    nums=[2,2,1,1,1,2,2]
    print(soln.majority_element(nums))