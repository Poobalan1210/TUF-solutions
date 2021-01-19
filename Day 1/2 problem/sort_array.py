class solution:
    def sort(self,arr):
        low , mid = 0,0
        high = len(arr)-1
        while mid <= high:

            if arr[mid] == 0:
                arr[low],arr[mid]=arr[mid],arr[low]
                mid+=1
                low+=1
            elif arr[mid] == 1:
                mid+=1
            elif arr[mid] == 2:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1
        print(arr)

if __name__ == "__main__":
    arr=[1,0,2,1,0,2,0,1,1,2,0]
    soln=solution()
    soln.sort(arr)