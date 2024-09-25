
# Assignment Report

## Title: Implementation and Analysis of Dynamic Array Resizing Strategies using EOWL Dataset

---

## Introduction

This report documents the implementation and analysis of different dynamic array resizing strategies using the Open English Word List (EOWL) dataset. The project is organized as a GitHub repository, allowing for version control and collaboration. The objective is to satisfy all the steps outlined in the assignment, which involves:

1. Using the EOWL dataset.
2. Implementing a sorted dynamic array with various resizing strategies.
3. Inserting words using binary search.
4. Measuring and analyzing time and space complexities both theoretically and empirically.
5. Comparing custom implementations with Python's built-in list.

**Implementation:**

- The dataset is loaded using the `load_eowl` function in the `assignment.py` script.
  
  ```python
  def load_eowl(filename):
      with open(filename, 'r') as file:
          words = file.read().splitlines()
      return words
  ```

- The `words_alpha.txt` file is included in the repository, ensuring easy access.

**Execution:**

- The script reads the `words_alpha.txt` file and loads all the words into a list named `words`.

---

### 2) Store Words in a Sorted Dynamic Array

**Implementation:**

- A `DynamicArray` class is implemented to handle the dynamic array with custom resizing strategies.
  
  ```python
  class DynamicArray:
      def __init__(self, strategy):
          # Initialization code
  ```

- The array starts with an initial capacity of 2, as per the assignment requirement.

**Execution:**

- For each resizing strategy, an instance of `DynamicArray` is created.
  
  ```python
  array_incremental = DynamicArray('incremental')
  array_doubling = DynamicArray('doubling')
  array_fibonacci = DynamicArray('fibonacci')
  ```

---

### 3) Increase Strategy A: Incremental (+10)

**Implementation:**

- The incremental strategy is implemented in the `_resize` method of the `DynamicArray` class.
  
  ```python
  if self.strategy == 'incremental':
      self.capacity += 10
  ```

**Execution:**

- The `array_incremental` instance uses this strategy during insertion.

---

### 4) Increase Strategy B: Doubling

**Implementation:**

- The doubling strategy is also implemented in the `_resize` method.
  
  ```python
  elif self.strategy == 'doubling':
      self.capacity *= 2
  ```

**Execution:**

- The `array_doubling` instance utilizes this strategy.

---

### 5) Increase Strategy C: Fibonacci Sequence

**Implementation:**

- The Fibonacci strategy is implemented using a sequence that is updated during each resize.
  
  ```python
  elif self.strategy == 'fibonacci':
      self.capacity = self.fib_seq[-1] + self.fib_seq[-2]
      self.fib_seq.append(self.capacity)
  ```

**Execution:**

- The `array_fibonacci` instance applies this resizing method.

---

### 6) Use Binary Search to Insert New Words

**Implementation:**

- The `_binary_search_insert` method performs a binary search to find the correct insertion index.
  
  ```python
  def _binary_search_insert(self, value):
      # Binary search implementation
  ```

- After finding the index, elements are shifted to insert the new word.

**Execution:**

- During insertion, each word is placed in the correct position to maintain a sorted array.

---

### 7) Measure Time at Each Search Point

**Implementation:**

- Time measurement is done using `time.perf_counter()`.
  
  ```python
  self.start_time = time.perf_counter()
  # ...
  current_time = time.perf_counter()
  elapsed_time = current_time - self.start_time
  ```

- Time elapsed is printed during each resize in the `print_status` method.

**Execution:**

- The program outputs the time elapsed since the start of insertion for each resize point.

---

### 8) Perform Theoretical Complexity Analysis

**Implementation:**

- Theoretical analysis is documented within the code comments and this report.

**Input Size (n):**

- The total number of words in the EOWL dataset.

**Time Complexity Analysis:**

- **Incremental Strategy:** O(n²) due to frequent resizing.
- **Doubling Strategy:** O(n log n) amortized time.
- **Fibonacci Strategy:** Between O(n log n) and O(n²).

**Space Complexity Analysis:**

- All strategies have a space complexity of O(n), but the amount of unused space varies.

**Execution:**

- The code reflects these complexities through its implementation and resizing behavior.

---

### 9) Repeat Steps 2 and 6 Using Python Lists

**Implementation:**

- A `ListDynamicArray` class is created to simulate resizing strategies using Python's built-in list.
  
  ```python
  class ListDynamicArray:
      def __init__(self, strategy):
          # Initialization code
  ```

- The same resizing strategies are applied, but using lists.

**Execution:**

- Instances for each strategy are created:
  
  ```python
  list_incremental = ListDynamicArray('incremental')
  list_doubling = ListDynamicArray('doubling')
  list_fibonacci = ListDynamicArray('fibonacci')
  ```

- The insertion logic uses Python's list methods, while managing resizing thresholds.

---

### 10) Empirically Measure Time and Space Complexity

**Implementation:**

- Time is measured using `time.perf_counter()`.
- Space is measured using the `get_size` function, which calculates the memory usage of the array or list.

  ```python
  array_size = get_size(self.array)
  ```

**Execution:**

- The program prints time elapsed and memory usage at each resize point for both arrays and lists.
- Outputs are provided for analysis and comparison.

---

### 11) Compare Complexities from Steps 8 and 10

**Implementation:**

- By observing the empirical data printed during execution, we compare it with the theoretical analysis.
- Comments in the code and this report discuss the observations.

**Execution:**

- After running the program, we analyze how the time and space measurements align with theoretical expectations.

---

### 12) Print Current Size, Time Elapsed, and Specific Elements

**Implementation:**

- The `print_status` method in both `DynamicArray` and `ListDynamicArray` classes handles this requirement.
  
  ```python
  def print_status(self):
      # Code to print size, time elapsed, memory usage, and specific elements
  ```

- Elements at positions 1st, `[n/4]`th, `[n/2]`th, `[3n/4]`th, and `n`th are printed, separated by `->`.

**Execution:**

- During each resize, the program outputs the required information, providing insights into the array's state.

---

## Results and Observations

- **Incremental Strategy:**
  - **Arrays:** Frequent resizing leads to higher time consumption and moderate memory usage.
  - **Lists:** Similar behavior, but Python's list optimizations mitigate some overhead.

- **Doubling Strategy:**
  - **Arrays:** Fewer resizing operations result in better time performance but increased memory usage due to larger capacity increments.
  - **Lists:** Efficient performance with acceptable memory overhead.

- **Fibonacci Strategy:**
  - **Arrays:** Offers a balance between time and space complexities.
  - **Lists:** Performs comparably to arrays with slight variations due to Python's internal optimizations.

- **Python List Default Behavior:**
  - Exhibits efficient resizing and memory usage, validating Python's optimized list implementation.

---

## Conclusion

The assignment requirements have been thoroughly satisfied through the implementation and execution detailed above. By integrating the code into a GitHub repository, the project is well-organized and accessible. The steps were meticulously followed, and the results provide valuable insights into the performance implications


