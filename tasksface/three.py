s=int(input())#mints kids have
n=int(input())#lenth of queue
sum=s
for i in range(1,n):
    p=sum-1
    sum=sum+p
print(sum)