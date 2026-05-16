import os
import random

def gen_element():

    key = random.randint(0, 10**7)
    return key

def gen_push():
    return (1, gen_element())
def gen_pop():
    return(2)
def gen_getTop():
    return (3)


def operation_sequences(filename, total_operations):
    with open(filename, 'w') as f:
        f.write(str(f"{total_operations}\n"))

        for i in range(total_operations):
            operation_to_perform = random.randint(1,3)

            if operation_to_perform == 1:
                operation_1 = gen_push()
                f.write(f"{operation_1[0]}\n")
                f.write(f"{operation_1[1]}\n")

            elif operation_to_perform == 2:
                operation_2 = gen_pop()
                f.write(f"{operation_2}\n")

            elif operation_to_perform == 3:
                operation_3 = gen_getTop()
                f.write(f"{operation_3}\n")

