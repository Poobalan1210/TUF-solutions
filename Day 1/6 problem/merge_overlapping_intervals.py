class Solution:
    def merge(self,arr):
        if not arr:
            print("[]")
        arr = sorted(arr,key=lambda x:x[0])
        interval=arr[0]
        res=[]
        for i in range(1,len(arr)):
            if interval[-1] < arr[i][0]:
                res.append(interval)
                interval=arr[i]
            else:
                interval[0] = min(interval[0],arr[i][0])
                interval[1] = max(interval[1],arr[i][1])
        res.append(interval)
        print(res)


if __name__ =="__main__":
    arr=[[1,3],[2,6],[8,10],[15,18]]
    soln=Solution()
    soln.merge(arr)