# ---------------------------------------------DATA STRUCTURE AND ALGORITHMS----------------------------------------------------------

# LISTS
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
print(my_list[0])    # Output: 1

my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(my_list)

# TUPLES
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple)
print(my_tuple[1])         # Output: 2

# SETS
my_set = {1, 2, 3, 4, 5, 6}
print(my_set)
my_set.add(7)

# DICTIONARIES
my_dict = {"name": "Santosh", "age": "20", "city": "Bathinda"};
print(my_dict)
print(my_dict["name"])

# STACKS
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)  # Output: [1, 2, 3, 4]
top_itme = stack.pop()
print(top_itme)        # Output: 4


# QUEUES
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)     # Output: deque([1, 2, 3, 4])
front_item = queue.popleft()
print(front_item)           # Output: 1


# LINKED LISTS
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


# SEARCHING AND SORTING ALGORITHMS
# LINEAR SEARCH
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# BINARY SEARCH
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= right:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# BUBBLE SORT
def bubble_sort(arr): 
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
my_list = [5, 2, 8, 12, 1]
bubble_sort(my_list)
print(my_list)  # Output: [1, 2, 5, 8, 12]


# MERGE SORT 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


# MEGER FUNCTION
def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Example usage:
my_list = [5, 2, 8, 12, 1]
merge_sort(my_list)
print(my_list)  # Output: [1, 2, 5, 8, 12]


