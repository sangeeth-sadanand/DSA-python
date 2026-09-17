## Array basic operations

import array

arr = array.array('i', [1, 2, 3, 4, 5])

# Array traversal
for i in arr:
    print(i)


# Array insertion
arr.append(6)  # Insert at the end
arr.insert(2, 10)  # Insert at index 2

print(arr)


# Array deletion
arr.remove(3)  # Remove first occurrence of value 3
del arr[1]  # Delete element at index 1 



import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Array traversal
for i in arr:
    print(i)

# Array insertion
arr = np.insert(arr, 2, 10)  # Insert 10 at index 2
print(arr)  

# array deletion
arr = np.delete(arr, 1)  # Delete element at index 1
print(arr)  

    