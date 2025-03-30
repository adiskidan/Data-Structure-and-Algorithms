arr = [12, 10, 9, 20, 1]

for i in range(len(arr)):
    max_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j
    if max_index != i:
        # Swap once
        arr[i], arr[max_index] = arr[max_index], arr[i]

print(arr)
