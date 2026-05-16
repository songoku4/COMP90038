import os
import time
from main import operation_sequences, competitior_array, max_heap, gen_element

def generate_push_file(filename, num_of_operations):
    with open (filename, 'w') as f:
        f.write(str(f"{num_of_operations}\n"))
        for i in range(num_of_operations):
            f.write(f"1\n")
            f.write(f"{gen_element()}\n")

def read_push_file(filename):
    keys_to_push = []
    with open(filename, 'r') as f:
        total_lines = f.readlines()
        i = 1
        while i < len(total_lines):
            