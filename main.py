import sys
import time
from random import randrange



if len(sys.argv) != 3:
    print("Invalid number of arguments")


open_data = open(sys.argv[2], "r")  # Fetch initialization values for the Memory Bus from a separate input file
open_instr = open (sys.argv[1], "r")  # Fetch instructions from an input file


# variable used to store values in  Memory Bus
memo_reg = {}

# Use ISA operand from instruction_input.txt as key to locate Source Register index position
# Line 1 in data_input.txt is R1 at index 0 etc.
# Index point is then used to retrieve or replace value
loca_address = {"R1": 0, "R2": 1, "R3": 2, "R4": 3, "R5": 4, "R6": 5, "R7": 6}


def time_delay():
    time.sleep(4)


# Send initial Memory Bus values to the CPU and Memory Bus and clearing memory
def cache(on_off):
    if on_off == '1':
        print("\nMemory before loading: ", memo_reg)
        print("\nLoading Memory...")

        time_delay()

        for line in open_data.readlines():
            memo_reg[line[:8]] = line[9]
        print("\nMemory loaded: ", memo_reg)
        print("\n")
    else:
        print("\nMemory before halt: ", memo_reg)
        print("\nClearing memory...")

        time_delay()

        memo_reg.clear()
        print("\nMemory after HALT: ", memo_reg)
        print("\n")
        open_data.close()


def write_to_register(value_in, reg_loc_in):
    print("->" * 20, 'Write to register initiated', "->" * 20)
    print("\nRegister before writing: ", memo_reg)

    time_delay()

    reg_address = value_from_cache([reg_loc_in])
    print(f"Value {value_in} to be updated in register address {reg_address[1]}")

    time_delay()
    memo_reg[reg_address[1]] = value_in

    print("\nRegister after writing: ", memo_reg)
    print("\n")
    print("<-" * 20, 'Register update successfully', "<-" * 20)
    time_delay()


def read_instructions(opcode):
    for line in opcode.readlines():
        inst_list = line.split()
        for item in inst_list:
            final_instr = item.split(',')
            if final_instr[0] in ['CACHE', 'HALT']:
                cache(final_instr[1])
            elif final_instr[0] == 'ADDI':
                addi(final_instr)
            elif final_instr[0] == 'ADD':
                add(final_instr)
            elif final_instr[0] == 'J':
                jump(final_instr[0])


def addi(opcode):
    print("*" * 40, "Addi Function initiated", "*" * 40)
    print('\nOpcode received in ADDI:', opcode)

    time_delay()

    dest, location, value_2 = opcode[1], opcode[2], opcode[3]
    value_1 = value_from_cache([location])
    answer = int(value_1[0][0]) + int(value_2)
    write_to_register(answer, dest)

    print(f"\nThe answer for {value_1[0]} + {value_2} is: {answer}")
    print("*" * 40, "Addi Function completed successfully", "*" * 40)
    print("\n")
    time_delay()


def add(opcode):
    print("*" * 40, "Add Function initiated", "*" * 40)
    print('\nOpcode received in ADD:', opcode)

    time_delay()

    dest, location_1, location_2 = opcode[1], opcode[2], opcode[3]
    value, reg_add = value_from_cache([location_1, location_2])
    print(f'Value is {value} and Reg Add is {reg_add}')
    answer = int(value[0]) + int(value[1])
    write_to_register(answer, dest)

    time_delay()

    print(f"\nThe answer for {value[0]} + {value[1]} is: {answer}")
    print("\n")
    print("*" * 40, "Add Function completed successfully", "*" * 40)
    print("\n")
    time_delay()


# jump instruction used to create
# simulation output
def jump(opcode):
    print("*" * 40, 'Jump Function initiated', "*" * 40)
    print(f"\nOpcode received in jump: {opcode}")

    time_delay()

    select_jump = randrange(0, 6)
    value = list(memo_reg.values())[select_jump]
    register = list(memo_reg.keys())[select_jump]
    print(f"\nUsing Jump function register went to register address {register} with Value {value}\n")
    print("*" * 40, "Jump Function completed succesfullly", "*" * 40)
    print("\n")
    time_delay()


def value_from_cache(locations):
    print("\n")
    print("@ " * 10, 'Retrieving information from register initiated', "@ " * 10)

    time_delay()

    values = []
    for location in locations:

        register = list(memo_reg)[loca_address[location]]
        values.append(list(memo_reg.values())[loca_address[location]])
        print(f"\nRetrieved value is {values} from location {register}.")

    time_delay()

    print('\n')
    print("@ " * 10, 'Information successfully retrieved', "@ " * 10)
    print("\n")
    print("*" * 20, 'Information sent to Operand', "*" * 20)
    print("\n")

    time_delay()

    return values, register


read_instructions(open_instr)
