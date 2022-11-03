import sys


print(len(sys.argv))

if len(sys.argv) != 3:
    print("Invalid number of arguments")


open_data = open(sys.argv[2], "r")  # Fetch initialization values for the Memory Bus from a separate input file
open_instr = open (sys.argv[1], "r")  # Fetch instructions from an input file


# variable used to store values in  Memory Bus
memo_reg = {}


# Send initial Memory Bus values to the CPU and Memory Bus and clearing memory
def cache(on_off):
    if on_off:
        print("\nMemory before loading: ", memo_reg)
        print("\nLoading Memory...")
        for line in open_data.readlines():
            memo_reg[line[:9]] = line[9]
            open_data.close()
        print("\nMemory loaded: ", memo_reg)
    if not on_off:
        print("\nMemory before halt: ", memo_reg)
        print("\nClearing memory...")
        memo_reg.clear()
        print("\nMemory after halt: ", memo_reg)


counter = 0


def write_to_register(data):
    global counter
    print("Memory before writing: ", memo_reg)
    if len(memo_reg) > 7:
        counter = 0


    print("Memory after writing: ", memo_reg)


# write_to_register(open_data)
