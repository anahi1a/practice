arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
m = 7 
n=len(arr)
if m==0 or n==0:
    print("nil")
arr.sort()
if(n<m):
    print("nil")

mindiff= arr[n-1] -arr[0]

for i in range(n-m+1): #i dont understand why n-m+1
    mindiff=min(mindiff,arr[i+m-1]-arr[i])
print(mindiff)

