import os
import sys
import time
from math import ceil

class DynamicArray:
    def _init_(self, strategy="Incremental"):
        self.size = 2  # Starting size of the dynamic array
        self.eowl = [None] * self.size
        self.count = 0
        self.strategy = strategy
        self.fib_n1 = 1  # For Fibonacci growth strategy
        self.fib_n2 = 1

    def resize(self):
        if self.strategy == "Incremental":
            self.size += 10
        elif self.strategy == "Doubling":
            self.size *= 2
        elif self.strategy == "Fib":
            new_size = self.fib_n1 + self.fib_n2
            self.fib_n1, self.fib_n2 = self.fib_n2, new_size
            self.size = new_size
        else:
            raise ValueError("Unknown resizing strategy!")
        
        # Create new array with updated size and copy existing elements
        new_eowl = [None] * self.size
        for i in range(self.count):
            new_eowl[i] = self.eowl[i]
        self.eowl = new_eowl

    def insert(self, word):
        if self.count == self.size:  # Array is full, resize
            self.resize()
        # Insert word into the next available position and maintain sorted order
        self.eowl[self.count] = word
        self.count += 1
        self.eowl[:self.count] = sorted(self.eowl[:self.count])  # Sort after insertion

    def _repr_(self):
        return str(self.eowl[:self.count])

def load_words(filepath):
    words = []
    with open(filepath, 'r') as f:
        for word in f.readlines():
            words.append(word.strip())
    return words

def test_growth_strategies():
    strategies = ["Incremental", "Doubling", "Fib"]
    filepath = "/Users/kprabhasreddy/Documents/GitHub/HW1_Fall24_C5115prog_kasireddy/words_alpha.txt"  # Update with actual path to the EOWL dataset file

    # Load the word list
    words = load_words(filepath)

    for strategy in strategies:
        print(f"\nTesting {strategy} strategy")
        dynamic_array = DynamicArray(strategy)
        start_time = time.time()

        for word in words:
            dynamic_array.insert(word)

        end_time = time.time()
        print(f"Time taken for {strategy} strategy: {end_time - start_time:.2f} seconds")
        print(f"Final array size: {dynamic_array.size}")
        print(f"Number of words stored: {dynamic_array.count}")

if __name__ == "_main_":
    test_growth_strategies()