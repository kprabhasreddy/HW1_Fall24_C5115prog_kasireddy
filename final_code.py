import time
import sys
import os

# Function to load the EOWL dataset
def load_eowl(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to get the size of an object (for memory usage)
def get_size(obj, seen=None):
    """Recursively finds the size of objects in bytes."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

# Dynamic Array Class using arrays
class DynamicArray:
    def __init__(self, strategy):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity
        self.strategy = strategy  # 'incremental', 'doubling', or 'fibonacci'
        self.fib_seq = [1, 2]  # Starting sequence for Fibonacci strategy
        self.start_time = time.perf_counter()
    
    def _resize(self):
        old_capacity = self.capacity
        
        if self.strategy == 'incremental':
            self.capacity += 10
        elif self.strategy == 'doubling':
            self.capacity *= 2
        elif self.strategy == 'fibonacci':
            self.capacity = self.fib_seq[-1] + self.fib_seq[-2]
            self.fib_seq.append(self.capacity)
        else:
            raise ValueError("Unknown strategy")
        
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        
        # Print status at each increase point
        self.print_status()
    
    def insert(self, value):
        if self.size == self.capacity:
            self._resize()
        
        # Binary search to find the correct index
        index = self._binary_search_insert(value)
        # Shift elements to make space
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1
    
    def _binary_search_insert(self, value):
        left, right = 0, self.size - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def print_status(self):
        n = self.size
        indices = [0, n // 4, n // 2, (3 * n) // 4, n - 1]
        elements = [self.array[i] for i in indices if i < n]
        current_time = time.perf_counter()
        elapsed_time = current_time - self.start_time
        array_size = get_size(self.array)
        print(f"Size: {self.capacity}, Time Elapsed: {elapsed_time:.5f}s, Memory Usage: {array_size} bytes, Elements: {' -> '.join(elements)}")

# ListDynamicArray class using Python lists
class ListDynamicArray:
    def __init__(self, strategy):
        self.capacity = 2
        self.array = []  # Use Python list
        self.strategy = strategy  # 'incremental', 'doubling', or 'fibonacci'
        self.fib_seq = [1, 2]
        self.resize_threshold = self.capacity
        self.start_time = time.perf_counter()
        self.resize_count = 0
    
    def _resize(self):
        old_capacity = self.capacity
        
        if self.strategy == 'incremental':
            self.capacity += 10
        elif self.strategy == 'doubling':
            self.capacity *= 2
        elif self.strategy == 'fibonacci':
            self.capacity = self.fib_seq[-1] + self.fib_seq[-2]
            self.fib_seq.append(self.capacity)
        else:
            raise ValueError("Unknown strategy")
        
        self.resize_threshold = self.capacity
        self.resize_count += 1
        # Print status at each increase point
        self.print_status()
    
    def insert(self, value):
        if len(self.array) >= self.resize_threshold:
            self._resize()
        
        # Binary search to find the correct index
        index = self._binary_search_insert(value)
        self.array.insert(index, value)
    
    def _binary_search_insert(self, value):
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def print_status(self):
        n = len(self.array)
        indices = [0, n // 4, n // 2, (3 * n) // 4, n - 1]
        elements = [self.array[i] for i in indices if i < n]
        current_time = time.perf_counter()
        elapsed_time = current_time - self.start_time
        array_size = get_size(self.array)
        print(f"Size: {self.capacity}, Time Elapsed: {elapsed_time:.5f}s, Memory Usage: {array_size} bytes, Elements: {' -> '.join(elements)}")

# Binary search for Python list (used in default implementation)
def binary_search_insert_python_list(array, value):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Insert words using Python list (default behavior)
def insert_words_python_list(words):
    eowl = []
    start_time = time.perf_counter()
    for idx, word in enumerate(words):
        index = binary_search_insert_python_list(eowl, word)
        eowl.insert(index, word)
        # Print status at powers of two sizes
        if (len(eowl) & (len(eowl) - 1) == 0):
            n = len(eowl)
            indices = [0, n // 4, n // 2, (3 * n) // 4, n - 1]
            elements = [eowl[i] for i in indices if i < n]
            current_time = time.perf_counter()
            elapsed_time = current_time - start_time
            list_size = get_size(eowl)
            print(f"Size: {len(eowl)}, Time Elapsed: {elapsed_time:.5f}s, Memory Usage: {list_size} bytes, Elements: {' -> '.join(elements)}")
    return eowl

# Main Execution
if __name__ == "__main__":
    # Ensure the dataset file exists
    filename = 'words_alpha.txt'
    if not os.path.isfile(filename):
        print(f"File '{filename}' not found. Please ensure it is in the same directory as this script.")
        exit(1)

    words = load_eowl(filename)
    
    # Limited the number of words 
    words = words[:1000]  # I reduced the number to only 1000 for faster execution

    # Strategy A: Incremental Increase (Arrays)
    print("\nStrategy A: Incremental Increase (Arrays)")
    array_incremental = DynamicArray('incremental')
    for word in words:
        array_incremental.insert(word)
    
    # Strategy B: Doubling (Arrays)
    print("\nStrategy B: Doubling (Arrays)")
    array_doubling = DynamicArray('doubling')
    for word in words:
        array_doubling.insert(word)
    
    # Strategy C: Fibonacci (Arrays)
    print("\nStrategy C: Fibonacci (Arrays)")
    array_fibonacci = DynamicArray('fibonacci')
    for word in words:
        array_fibonacci.insert(word)
    
    # Strategy A: Incremental Increase (Lists)
    print("\nStrategy A: Incremental Increase (Lists)")
    list_incremental = ListDynamicArray('incremental')
    for word in words:
        list_incremental.insert(word)
    
    # Strategy B: Doubling (Lists)
    print("\nStrategy B: Doubling (Lists)")
    list_doubling = ListDynamicArray('doubling')
    for word in words:
        list_doubling.insert(word)
    
    # Strategy C: Fibonacci (Lists)
    print("\nStrategy C: Fibonacci (Lists)")
    list_fibonacci = ListDynamicArray('fibonacci')
    for word in words:
        list_fibonacci.insert(word)
    
    # Python List (Default Behavior)
    print("\nPython List Implementation (Default Behavior)")
    eowl_list = insert_words_python_list(words)
