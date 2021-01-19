class Solution:
    def max_sum(self,arr):
        max=arr[0]
        sum=0
        i=0
        while i < len(arr):
            sum += arr[i]
            if sum > max:
                max=sum
            if sum < 0:
                sum = 0
            i+=1
        print(max)
if __name__ == "__main__":
    arr=[-2,-3,4,-1,-2,1,5,-3]
    soln=Solution()
    soln.max_sum(arr)