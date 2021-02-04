
class solution:

    def __init__(self):
        self.count=0

    def inversion_of_array(self,n):
        print(self.mergesort(n))
        print(self.count)
    
    def mergesort(self,n):
        if len(n) > 1:
            mid=len(n)//2
            l=n[:mid]
            r=n[mid:]

            self.mergesort(l)
            self.mergesort(r)

            i=j=k=0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    n[k] = l[i]
                    i+=1
                else:
                    n[k]=r[j]
                    j+=1
                    self.count+=1
                k+=1

            while i < len(l):
                n[k] = l[i]
                k+=1
                i+=1

            while j < len(r):
                n[k] = r[j]
                k+=1
                j+=1

        return n

if __name__ == "__main__":
    soln=solution()
    n=[8,4,2,1]
    soln.inversion_of_array(n)