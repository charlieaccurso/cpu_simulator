class Clock:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1

class ControlUnit:
    def __init__(self, cpu, clock):
        self.cpu = cpu
        self.clock = clock

    def fetch(self, pc):
        return self.cpu.memory.memory[pc]

    def decode(self, instruction):
        return self.cpu.decoder.decode(instruction)

    def execute(self, instruction_name, operands):
        if instruction_name == "LOAD":
            src_address, dest_register = operands
            self.cpu.LOAD(int(src_address), dest_register)

        elif instruction_name == "ADD":
            src_reg1, src_reg2, dest_register = operands
            self.cpu.ADD(src_reg1, src_reg2, dest_register)

        elif instruction_name == "STORE":
            src_register, dest_address = operands
            self.cpu.STORE(src_register, int(dest_address))

        elif instruction_name == "HALT":
            self.cpu.HALT()
            return False

        return True


class Memory:
    def __init__(self, size=32):
        # each location stores a 32-bit integer
        self.memory = [0 for _ in range(size)]

class Registry:
    def __init__(self, size=8):
        # Each location stores a 32-bit integer with register names as keys
        self.registry = {f'R{i}': 0 for i in range(size)}

class Decoder:
    def decode(self, instruction):
        instruction_parts = instruction.split()
        instruction_name = instruction_parts[0]
        operands = [operand.strip(',') for operand in instruction_parts[1:]]
        return instruction_name, operands
    
class ProgramLoader:
    def __init__(self, memory):
        self.memory = memory

    def load_program(self, program):
        for address, instruction in enumerate(program):
            if isinstance(instruction, int):
                self.memory.memory[address] = str(instruction)  # Convert integer to string
            else:
                self.memory.memory[address] = instruction