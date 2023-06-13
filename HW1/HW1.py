arr = [1,12,5,32,56,7,15,0]
print(*arr)
def change(arr, n, i):
    temp = i
    l = 2 * i + 1  
    r = 2 * i + 2;   
    if l < n and arr[i] < arr[l]:
        temp = l
    if r < n and arr[temp] < arr[r]:
        temp = r
    if temp != i:
        arr[i], arr[temp] = arr[temp],arr[i] 
        change(arr, n, temp)

def sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        change(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        change(arr, i, 0)

sort(arr)
print(*arr)
