#shortcut method
str1 = "hello world whats up"
str1=str1.split(" ")
for i in str1[::-1]:
    print(i, end=" ")

#iterative way
A = "hello world whats up"
A=A.split(" ")
start=0
end=len(A)-1
while start<end:
    temp = A[start]
    A[start]=A[end]
    A[end]=temp
    #A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

print(A)

for i in A:
    print(i, end=" ")

