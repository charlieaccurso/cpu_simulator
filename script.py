# script.py
from cpu import CPU

cpu = CPU()

# Create a list of instructions representing the program
program = [
    "LOAD 5, R3",      # Load the value from memory address 5 into R3
    "LOAD 6, R4",      # Load the value from memory address 6 into R4
    "ADD R3, R4, R2",  # Add the values in R3 and R4 and store in R2
    "STORE R2, 7",     # Store the value from R2 into memory address 7
    "HALT"             # Halt the program
]

cpu.memory.memory[5] = 2
cpu.memory.memory[6] = 13

# Load and execute the program
cpu.run(program)

# Display the memory and registers after execution
cpu.display_memory()
cpu.display_registers()


