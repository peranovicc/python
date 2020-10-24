from tqdm import tqdm

def binary_search(arr,low,high,k,bar):
    bar.update(1)
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid + 1
        if arr[mid] < k:
            return binary_search(arr,mid+1,high,k,bar)
        if arr[mid] > k:
            return binary_search(arr,low,mid-1,k,bar)
    
    else:
        return -1

fi = open('binary.txt','r')

n = int(fi.readline())
bar = tqdm(total = n)
m = int(fi.readline())
arr = [int(x) for x in fi.readline().split()]
ks = [int(x) for x in fi.readline().split()]

fo = open('binaryOut.txt','w')
fo.write(' '.join(str(binary_search(arr,0,len(arr)-1,k,bar)) for k in ks))
