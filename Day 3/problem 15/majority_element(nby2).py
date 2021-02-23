class solution:
    def majority_element(self,nums):
        from collections import Counter
        counter=Counter(nums)
        maxi=0
        val=0
        for key in counter.keys():
            # print('keys :'+str(key))
            if counter[key] > maxi:
                maxi=counter[key]
                val=key
                # print(maxi)
        return val



if __name__ =="__main__":
    soln=solution()
    nums=[2,2,1,1,1,2,2]
    print(soln.majority_element(nums))