# cpu.py
from components import Memory, Registry, Decoder, ControlUnit, Clock, ProgramLoader

class CPU:
    def __init__(self):
        self.memory = Memory()
        self.registry = Registry()
        self.decoder = Decoder()
        self.clock = Clock()

    def LOAD(self, src_address, dest_register):
        # Implementation of the LOAD operation (same as before)
        data = self.memory.memory[src_address]
        print(f"LOAD DATA: {data}")
        self.registry.registry[dest_register] = data

    def ADD(self, src_reg1, src_reg2, dest_register):
        # Implementation of the ADD operation (same as before)
        result = self.registry.registry[src_reg1] + self.registry.registry[src_reg2]
        self.registry.registry[dest_register] = result

    def STORE(self, src_register, dest_address):
        # Implementation of the STORE operation
        data = self.registry.registry[src_register]
        self.memory.memory[dest_address] = data

    def HALT(self):
        # Implementation of the HALT operation (same as before)
        print("Program halted.")

    def run(self, program):
        # Load the program into memory using the ProgramLoader
        program_loader = ProgramLoader(self.memory)
        program_loader.load_program(program)

        pc = 0
        control_unit = ControlUnit(self, self.clock)  # Pass the CPU instance and clock instance to ControlUnit
        while True:
            # Fetch: Get the instruction from memory using the PC
            instruction = control_unit.fetch(pc)

            # Decode: Get the instruction name and operands using the decoder
            instruction_name, operands = control_unit.decode(instruction)

            print(f"OPERANDS ARE: {operands}")

            # Execute: Perform the operation based on the instruction name and operands
            continue_execution = control_unit.execute(instruction_name, operands)
            if not continue_execution:
                break

            # Update PC: Move to the next instruction in memory
            pc += 1

            # Increment the clock time
            self.clock.tick()

    def display_memory(self):
        print("Memory:")
        for i, value in enumerate(self.memory.memory):
            print(f"Address {i}: {value}")
        print()

    def display_registers(self):
        print("Registers:")
        for register_name, value in self.registry.registry.items():
            print(f"{register_name}: {value}")
        print()
