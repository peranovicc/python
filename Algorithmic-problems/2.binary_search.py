
def binary_search(arr,low,high,k):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid + 1
        if arr[mid] < k:
            return binary_search(arr,mid+1,high,ks)
        if arr[mid] > k:
            return binary_search(arr,low,mid-1,k)
    
    else:
        return -1

fi = open('binary.txt','r')

n = int(fi.readline())
m = int(fi.readline())
arr = [int(x) for x in fi.readline().split()]
ks = [int(x) for x in fi.readline().split()]

fo = open('binaryOut.txt','w')
fo.write(' '.join(str(binary_search(arr,0,len(arr)-1,k)) for k in ks))
