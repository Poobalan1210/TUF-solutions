class Solution:
    def merge_sorted_arr(self,arr1,arr2):
        i=0
        j=0
        while i < len(arr1):
            if arr1[i] < arr2[j]:
                i+=1
            elif arr1[i] > arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
                i+=1
                arr2.sort()
        print(arr1,arr2)


if __name__ == "__main__":
    arr1=[1,3,4,6,10]
    arr2=[2,5,9]
    soln=Solution()
    soln.merge_sorted_arr(arr1,arr2)