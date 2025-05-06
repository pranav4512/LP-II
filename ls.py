def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the element is found
    return -1  # Return -1 if not found

# Example usage
numbers = [5, 3, 8, 6, 1]
target = 6

result = linear_search(numbers, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
  
