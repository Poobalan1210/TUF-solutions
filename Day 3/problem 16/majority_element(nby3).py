class solution:
    def majority_element(self,nums):
        from collections import Counter
        counter=Counter(nums)
        output=[]
        for key in counter.keys():
            if counter[key] > len(nums)/3:
                output.append(key)
        return output


if __name__ =="__main__":
    soln=solution()
    nums=[3,2,3]
    print(soln.majority_element(nums))