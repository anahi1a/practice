#first approach
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        h={}
        for n in range(1,len(A)+1):
            h[n]=0
        for i in A:
            if i in h:
                h[i]+=1
        for k,v in h.items():
            if v==0:
                miss=k
            if v==2:
                rep=k
        return [rep,miss]
