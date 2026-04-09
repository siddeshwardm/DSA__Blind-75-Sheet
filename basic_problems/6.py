def function(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    function(arr,left+1,right-1)

arr = int(input("enter the number:"))
arr = list(str(arr))
function(arr,0,len(arr)-1)
print(arr)    