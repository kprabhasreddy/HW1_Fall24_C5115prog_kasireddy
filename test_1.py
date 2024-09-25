import time
import bisect
import requests

# Load the EOWL dataset
def load_eowl():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    response = requests.get(url)
    words = response.text.splitlines()
    return sorted(words)

# Dynamic array class with different growth strategies
class DynamicArray:
    def __init__(self, strategy='incremental'):
        self.array = [None] * 2
        self.size = 0
        self.capacity = 2
        self.strategy = strategy
        self.fib_seq = [1, 2]

    def _resize(self):
        if self.strategy == 'incremental':
            self.capacity += 10
        elif self.strategy == 'doubling':
            self.capacity *= 2
        elif self.strategy == 'fib':
            self.capacity = self.fib_seq[-1] + self.fib_seq[-2]
            self.fib_seq.append(self.capacity)
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, word):
        if self.size == self.capacity:
            self._resize()
        # Insert the word into the sorted portion of the array
        bisect.insort(self.array[:self.size], word)
        # Move the elements back to the main array
        self.array = self.array[:self.size] + [word] + [None] * (self.capacity - self.size - 1)
        self.size += 1

    def __getitem__(self, index):
        if index < self.size:
            return self.array[index]
        raise IndexError('Index out of range')

    def __len__(self):
        return self.size

# Measure time and print elements at each increase point
def measure_time_and_print(array, words):
    start_time = time.time()
    for i, word in enumerate(words):
        array.insert(word)
        if i == array.capacity - 1:
            elapsed_time = time.time() - start_time
            n = len(array)
            print(f"Size: {n}, Time: {elapsed_time:.4f}s, Elements: {array[0]} -> {array[n//4]} -> {array[n//2]} -> {array[3*n//4]} -> {array[n-1]}")

# Main function
def main():
    words = load_eowl()
    strategies = ['incremental', 'doubling', 'fib']
    for strategy in strategies:
        print(f"\nStrategy: {strategy.capitalize()}")
        array = DynamicArray(strategy=strategy)
        measure_time_and_print(array, words)

if __name__ == "__main__":
    main()
