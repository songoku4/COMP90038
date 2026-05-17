import os
import time
from main import operation_sequences, competitior_array, max_heap, gen_element

DATA_DIR = "experiment_1_data"

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

def test_experiment4_files(filename):
    print(f"Testing:" , filename)
    keys_to_push = read_push_file(filename)

    total_heapify_time = 0
    total_push_time = 0
    runs = 5

    for i in range(runs):
        #Method 1: Heapify(σ)
        start_heapify = time.perf_counter()
        empty_max_heap = max_heap()

        collected_elements = keys_to_push.copy()

        #Heapifying the collected elements
        empty_max_heap.heapify(collected_elements)

        end_heapify = time.perf_counter()
        total_heapify_time = total_heapify_time + (end_heapify - start_heapify)

        #Method 2: push-one-by-one(σ)
        start_push = time.perf_counter()
        empty_max_heap_2 = max_heap()

        #Invoking H.push(key) for each push operation in σ
        for key in keys_to_push:
            empty_max_heap_2.push(key)

        end_push = time.perf_counter()
        total_push_time = total_push_time + (end_push - start_push)

        average_heapify_time_micro = (total_heapify_time / runs) * 10**6
        average_push_time_micro = (total_push_time / runs) * 10**6

    print("Average Heapify Time: ", round(average_heapify_time_micro, 2), "microseconds")
    print("Average Push-by-Push Time: ", round(average_push_time_micro, 2), "microseconds")


if __name__ == "__main__":
    test_experiment4_files("experiment1_0.1M.txt")
    test_experiment4_files("experiment1_0.2M.txt")
    test_experiment4_files("experiment1_0.5M.txt")
    test_experiment4_files("experiment1_0.8M.txt")
    test_experiment4_files("experiment1_1.0M.txt")
