# bubble sort using recursion

arr = [3,5,2,8,1]
n = len(arr)
# this recursive function makes the largest element get to the end 
def bubUp(arr,q,j):
    if j == q:
        return arr
    if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
    return bubUp(arr,q,j+1)
# this function basically calls the bubUp function again and again 
def sort(arr,i,j):
    if i==n-1:
        return arr
    else:
        arr = bubUp(arr,n-i-1,0)
        return sort(arr,i+1,j)
    
print(sort(arr,0,0))


#github: ozamaahmed

