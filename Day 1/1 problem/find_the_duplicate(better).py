class solution:
    def findDuplicate(self,nums):
        from collections import Counter
        d=dict(Counter(nums))
        for i,j in d.items():
            if j > 1:
                return i


if __name__ =="__main__":
    nums=[1,2,4,5,6,1,3]
    soln=solution()
    print(soln.findDuplicate(nums))