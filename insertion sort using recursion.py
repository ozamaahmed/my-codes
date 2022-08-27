# insertion sort using recursion

arr = [1,2,6,7,3,0,19,-4,4,3]
n = len(arr)
#this fucnction basically takes the key and keeps swapping
# it until theres a smaller element before it 
def swapper(arr,j,key):
    if j<=-1 or arr[j]<key:
        arr[j+1] = key
        return arr
    else:
        if arr[j]>=key:
            arr[j+1] = arr[j]
            return swapper(arr,j-1,key)
#and this function calls the swapper for every i
def recInSort(arr,i):
    if i==n:
        return arr
    else:
        arr = swapper(arr,i-1,arr[i])
        return recInSort(arr,i+1)
        
print(recInSort(arr,1))
