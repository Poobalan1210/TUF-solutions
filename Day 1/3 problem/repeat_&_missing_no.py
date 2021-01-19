class Solution:
    def find_missing(self,arr):
        from collections import Counter
        counter=dict(Counter(arr))
        for i in range(1,len(arr)+1):
            if i not in counter.keys():
                missing = i
            elif counter[i] > 1:
                repeated = i
        print(f"Missing is -{missing} Repeated no is -{repeated}")
        

if __name__ == "__main__":
    arr=[1,5,6,3,4,2,6]
    soln=Solution()
    soln.find_missing(arr)