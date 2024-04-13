
 def missingNumber(self,array,n):
        # code here
        mean=(n*(n+1))//2
        total=sum(array)
        return mean-total
