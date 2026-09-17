from collections.abc import Iterator
from typing import Iterable, Any
import math



def linear(arr: Iterable, target: Any):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary(arr: Iterable, target):
    start = 0 
    end = len(arr) - 1
    while start < end:
        delta = (end - start + 1) // 2
        mid = start + delta
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid
        elif arr[mid] < target:
            start = mid
    else: 
        return -1


def jump(arr: Iterable, target):
    jump = math.ceil(math.sqrt(len(arr)))
    length = len(arr)
    start = 0 
    while start + jump < len(arr):
        if arr[start] <= target and target <= arr[start+jump]:
            break
        if arr[start] > target:
            return -1
        start += jump
    end = min(start + jump +1, length)
    index = linear(arr[start:], target)
    return index + start


def interpolation(arr, target):
    if target > arr[-1] or target < arr[0]:
        return -1 
    slope = (len(arr)-1) / (arr[-1] - arr[0])
    index = slope * (target - arr[0])
    index = int(round(index,0))
    if arr[index] != target:
        return -1
    return index

def exponential(arr: Iterable, target):
    jump = 1
    length = len(arr)
    start = 0 
    while start + jump < len(arr):
        if arr[start] <= target and target <= arr[start+jump]:
            break
        if arr[start] > target:
            return -1
        jump *= 2
        start += jump
    end = min(start + jump +1, length)
    index = binary(arr[start:], target)
    return index + start



if __name__ == "__main__":
    import timeit
    arr = list(range(1, 20000))  # Create an array with elements from 1 to 10
    target = arr[-1] # Target is the last element in the array

    functions = [linear , binary, jump, interpolation, exponential]
    functions = [ ternary ]
    

    # Measure the execution time of the linear search function
    for func in functions:
        index = func(arr, target)
        print(index, target, arr[index])
        execution_time = timeit.timeit(lambda: func(arr, target), number=10000)
        print(f"Execution time for {func.__name__} search: {execution_time} seconds")    

