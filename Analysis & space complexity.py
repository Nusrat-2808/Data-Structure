def sum(n):
    return n*(n+1)/2
#Space complexity:0(1),Auxiliary space=0(1) Linear space:
def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return(sum)
a=[12,3,4,15]
arraysum(a)
#with the size of the array,the space also required increases
#space complexity:0(n),Auxiliary space=0(1)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(4))
def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
numbers=[1, 3, 5, 7, 9, 11, 13]
target=7
result= binary_search(numbers,target)
if result !=-1 :
    print(f"Element found at index {result}")
else:
    print("Element not found")