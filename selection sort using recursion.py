# selection sort 

# def selsort(arr):
#     n = len(arr)
#     for i in range(n):
#         min = i
#         for j in range(i,n):
#             if arr[j]<arr[min]:
#                 arr[j],arr[min] = arr[min],arr[j]
#     return arr
# arr = [3,2,-5,1,4,5,-3]
# print(selsort(arr))


arr = [3,2,-5,1,4,5,-3]
n = len(arr)
# def select(arr,i,min):
#     if i==n-1:
#         return arr
#     else:
#         min = i
#         if arr[i]<arr[min]:
#             arr[i],arr[min] = arr[min],arr[i]
#         arr = select(arr,i+1,min)
#     return arr

# print(select(arr,0,0))









# def tra(arr,i):
#     if i==n:
#         return arr
#     else:
#         arr[i] = arr[i]+2
#     return tra(arr,i+1)

# print(tra(arr,0))



def findmin(arr,i,m):
    if i==n:
        return m
    else:
        if arr[i]<arr[m]:
            m = i
        return findmin(arr,i+1,m)
def selsort(arr,j,m):
    if j==n-1:
        return arr
    else:
        m = findmin(arr,j,m)
        arr[m],arr[j] = arr[j],arr[m]
        return selsort(arr,j+1,m)
print(selsort(arr,0,0))


