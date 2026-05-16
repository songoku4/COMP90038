import os
import time
import random
from main import operation_sequences, competitior_array, max_heap, gen_element

DATA_DIR = "experiment_2_data"
os.makedirs(DATA_DIR, exist_ok=True)

def generate_experiment2_file(filename, num_of_operations, probability_of_getTop):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(str(f"{num_of_operations}\n"))
        for i in range(num_of_operations):
            if random.random() < probability_of_getTop:
                f.write("3\n")
            else:
                f.write(f"1 {gen_element()}\n")

def read_experiment2_file(filename):
    operations = []
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        total_lines = f.readlines()
        for i in range(1, len(total_lines)):
            split = total_lines[i].split()
            operation_type = int(split[0])

            if operation_type == 1:
                key = int(split[1])
                operations.append((1, key))
            elif operation_type == 3:
                operations.append((3, None))
    return operations

def test_experiment2_files(filename):
    print(f"Testing:" , filename)
    operations_from_file = read_experiment2_file(filename)

    total_array_time = 0
    total_heap_time = 0
    runs = 5

    for i in range(runs):
        array = competitior_array()
        start_array = time.perf_counter()
        for curr_operation in operations_from_file:
            if curr_operation[0] == 1:
                array.push(curr_operation[1])
            elif curr_operation[0] == 3:
                array.getTop()
        end_array = time.perf_counter()
        total_array_time = total_array_time + (end_array - start_array)

        heap = max_heap()
        start_heap = time.perf_counter()
        for curr_operation in operations_from_file:
            if curr_operation[0] == 1:
                heap.push(curr_operation[1])
            elif curr_operation[0] == 3:
                heap.getTop()
        end_heap = time.perf_counter()
        total_heap_time = total_heap_time + (end_heap - start_heap)

    average_array_time_micro = (total_array_time / runs) * 10**6
    average_heap_time_micro = (total_heap_time / runs) * 10**6

    print("Average Array Time: ", round(average_array_time_micro, 2), "microseconds")
    print("Average Heap Time: ", round(average_heap_time_micro, 2), "microseconds")

if __name__ == "__main__":

    generate_experiment2_file("experiment2_0.1_percent.txt", 10**6, 0.01)
    test_experiment2_files("experiment2_0.1_percent.txt")

    generate_experiment2_file("experiment2_0.5_percent.txt", 10**6, 0.05)
    test_experiment2_files("experiment2_0.5_percent.txt")

    generate_experiment2_file("experiment2_1.0_percent.txt", 10**6, 0.1)
    test_experiment2_files("experiment2_1.0_percent.txt")

    generate_experiment2_file("experiment2_5.0_percent.txt", 10**6, 0.05)
    test_experiment2_files("experiment2_5.0_percent.txt")

    generate_experiment2_file("experiment2_10.0_percent.txt", 10**6, 0.10)
    test_experiment2_files("experiment2_10.0_percent.txt")