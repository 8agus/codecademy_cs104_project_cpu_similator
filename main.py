import sys


if len(sys.argv) != 3:
    print("Invalid number of arguments")


open_data = open(sys.argv[2], "r")  # Fetch initialization values for the Memory Bus from a separate input file
open_instr = open (sys.argv[1], "r")  # Fetch instructions from an input file


# variable used to store values in  Memory Bus
memo_reg = {}


# Send initial Memory Bus values to the CPU and Memory Bus and clearing memory
def cache(on_off):
    if on_off == '1':
        print("\nMemory before loading: ", memo_reg)
        print("\nLoading Memory...")
        for line in open_data.readlines():
            memo_reg[line[:8]] = line[9]
        print("\nMemory loaded: ", memo_reg)
        print("\n")
    else:
        print("\nMemory before halt: ", memo_reg)
        print("\nClearing memory...")
        memo_reg.clear()
        print("\nMemory after HALT: ", memo_reg)
        print("\n")
        open_data.close()


counter = 0


def write_to_register(data):
    global counter
    print("Memory before writing: ", memo_reg)
    if len(memo_reg) > 7:
        counter = 0


    print("Memory after writing: ", memo_reg)

instruction_list = []


def read_instructions(opcode):
    for line in opcode.readlines():
        inst_list = line.split()
        for item in inst_list:
            final_instr = item.split(',')
            print(final_instr, 'Line 52')
            if final_instr[0] in ['CACHE', 'HALT']:
                print('Line 56: ', final_instr[0])
                cache(final_instr[1])
            elif final_instr[0] == 'ADDI':
                addi(final_instr)


def addi(opcode):
    print('\nOpcode received in ADDI:', opcode)
    dest, location, value_2 = opcode[1], opcode[2], opcode[3]
    value_1 = value_from_cache([location])
    answer = int(value_1) + int(value_2)
    return print(f"\nThe answer for {value_1} + {value_2} is: {answer}")


def value_from_cache(locations):
    values = []
    loca_address = {
        "R1": 0,
        "R2": 1,
        "R3": 2,
        "R4": 3,
        "R5": 4,
        "R6": 5,
        "R7": 6,
    }
    for location in locations:
        print("Line 82: ", location)
        print("Line 83: ", loca_address[location])
        register = list(memo_reg)[loca_address[location]]
        values = list(memo_reg.values())[loca_address[location]]
        print(f"\nRetrieved value is {values} from location {register}.")

    return values


read_instructions(open_instr)
