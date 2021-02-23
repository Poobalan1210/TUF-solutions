class solution:
    def majority_element(self,nums):
        
        num1,num2,count1,count2=-1,-1,0,0
        for element in nums:
            if element == num1:
                count1+=1;
            elif element == num2:
                count2+=1
            elif count1 == 0:
                num1=element
                count1=1
            elif count2 == 0:
                num2=element
                count2=1
            else:
                count1-=1
                count2-=1
        
        answer=[]
        count1,count2=0,0
        for element in nums:
            if element == num1:
                count1+=1
            if element == num2:
                count2+=1
        
        if count1 > len(nums)/3:
            answer.append(num1)
        if count2 > len(nums)/3:
            answer.append(num2)
        
        answer=set(answer)
        return list(answer)


if __name__ =="__main__":
    soln=solution()
    nums=[3,2,3]
    print(soln.majority_element(nums))