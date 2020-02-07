def quicksort(array, start, end):
    if(start>=end):
        return
    p = partition(array, start, end)
    quicksort(array, start, p-1)
    quicksort(array, p+1, end)

def partition(arr, start, end):
    pivot=arr[start]
    low=start+1
    high=end
    while True:
        while low<=high and arr[high]>=pivot:
            high-=1
        while low<=high and arr[low]<=pivot:
            low+=1
        if low<=high:
            arr[low],arr[high]=arr[high],arr[low]
        else:
            break
    arr[start],arr[high]=arr[high],arr[start]
    return arr

google=[7,9,10,24,6]
# quicksort(google)