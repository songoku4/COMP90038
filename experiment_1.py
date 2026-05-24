# Name: Aaditya Sharma
# Student ID: 1814346
# COMP90038 Assignment 2
# Description: Conducted Experiment 1 to compare the running time of a Competitor Array and a Max-Heap for push-only sequences of varying lengths.
import os
import time
from main import operation_sequences, competitior_array, max_heap, gen_element

# Create the directory for storing generated sequence files
DATA_DIR = "experiment_1_data"
os.makedirs(DATA_DIR, exist_ok=True)

def generate_push_file(filename, num_of_operations):
    filepath = os.path.join(DATA_DIR, filename)
    with open (filepath, 'w') as f:
        f.write(str(f"{num_of_operations}\n"))
        for i in range(num_of_operations):
            f.write(f"1 {gen_element()}\n")

def read_push_file(filename):
    keys_to_push = []
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        total_lines = f.readlines()
        i = 1
        while i < len(total_lines):
            split = total_lines[i].split()
            operation_type = int(split[0])
            if operation_type == 1:
                key = int(split[1])
                keys_to_push.append(key)
                i = i + 1
    return keys_to_push

def test_structures(filename):
    print(f"Testing:" , filename)
    keys_to_push = read_push_file(filename)

    total_array_time = 0
    total_heap_time = 0
    runs = 5

    for i in range(runs):
        # Time the Competitor Array
        array = competitior_array()
        start_array = time.perf_counter()
        for key in keys_to_push:
            array.push(key)
        end_array = time.perf_counter()
        total_array_time = total_array_time + (end_array - start_array)
# Time the Max-Heap
        heap = max_heap()
        start_heap = time.perf_counter()
        for key in keys_to_push:
            heap.push(key)
        end_heap = time.perf_counter()
        total_heap_time = total_heap_time + (end_heap - start_heap)

    
    #Calculating average and converting time to microseconds

    average_array_time_micro = (total_array_time / runs) * 10**6
    average_heap_time_micro = (total_heap_time / runs) * 10**6

    print("Average Array Time: ", round(average_array_time_micro, 2), "microseconds")
    print("Average Heap Time: ", round(average_heap_time_micro, 2), "microseconds")


if __name__ == "__main__":
    #Generating push-only sequences
    #0.1 Million
    generate_push_file("experiment1_0.1M.txt", 10**5)
    test_structures("experiment1_0.1M.txt")

    #0.2 Million
    generate_push_file("experiment1_0.2M.txt", 2 * 10**5)
    test_structures("experiment1_0.2M.txt")

    #0.5 Million
    generate_push_file("experiment1_0.5M.txt", 5 * 10**5)
    test_structures("experiment1_0.5M.txt")

    #0.8 Million
    generate_push_file("experiment1_0.8M.txt", 8 * 10**5)
    test_structures("experiment1_0.8M.txt")

    #1.0 Million
    generate_push_file("experiment1_1.0M.txt", 10**6)
    test_structures("experiment1_1.0M.txt")