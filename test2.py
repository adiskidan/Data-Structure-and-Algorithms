arr = [12, 10, 9, 20, 1]
i=0
while i<len(arr):
    max_index = i
    j=i+1
    while j<len(arr):
        if arr[j] > arr[max_index]:
            max_index = j
        j+=1
    if max_index != i:
        # Swap once
        arr[i], arr[max_index] = arr[max_index], arr[i]
    i+=1
print(arr)
