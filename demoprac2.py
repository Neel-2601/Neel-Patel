import sys

arr = list(map(int, input("Enter the Numbers : ").split()))
m=arr[0]
n=len(arr)

if(n<2):
    print("Enter value of two array")
    sys.exit(0)


for i in range (n-1):
    for j in range(i+1,n):
        sum=arr[i]+arr[j]
        if(sum<0):
            sum*=-1
        if m>sum:
            m=sum
            num1=arr[i]
            num2=arr[j]

print("Two numbers whose sum in nearest zero are:", num1,num2)
