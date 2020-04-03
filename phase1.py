from bitstring import BitArray

dict_of_format = {
	# instructions of I-Format
	'andi': ['I', '0010011', '111'],
	'addi': ['I', '0010011', '000'],
	'ori': ['I', '0010011', '110'],
	'lb': ['I', '0000011', '000'],
	'lh': ['I', '0000011', '001'],
	'lw': ['I', '0000011', '010'],
	'ld': ['I', '0000011', '011'],
	'jalr': ['I', '1100111', '000'],

	# instructions of S-Format
	'sb': ['S', '0100011', '000'],
	'sh': ['S', '0100011', '001'],
	'sw': ['S', '0100011', '010'],
	'sd': ['S', '0100011', '011'],

	# instructions of R-Format
	'add': ['R', '0110011', '000', '0000000'],
	'and': ['R', '0110011', '111', '0000000'],
	'or': ['R', '0110011', '110', '0000000'],
	'sub': ['R', '0110011', '000', '0100000'],
	'mul': ['R', '0110011', '000', '0000001'],
	'div': ['R', '0110011', '100', '0000001'],
	'sll': ['R', '0110011', '001', '0000000'],
	'slt': ['R', '0110011', '010', '0000000'],
	'xor': ['R', '0110011', '100', '0000000'],
	'srl': ['R', '0110011', '101', '0000000'],
	'sra': ['R', '0110011', '101', '0100000'],
	# 'rem':['R','','','']

	# instructions of U-Format
	'lui': ['U', '0110111'],
	'auipc': ['U', '0010111'],

	# instructions of SB-Format
	'beq': ['SB', '1100011', '000'],
	'bne': ['SB', '1100011', '001'],
	'blt': ['SB', '1100011', '100'],
	'bge': ['SB', '1100011', '101'],

	# instructions of UJ-Format
	'jal': ['UJ', '1101111'],

	# instruction for breakpoint
	'breakpoint': ['special','0000000','000','0000000']
}
input_filepath = './input/input.asm'


def R_Type(instruction):
	instruction = instruction.split()
	opcode = dict_of_format[instruction[0]][1]
	funct3 = dict_of_format[instruction[0]][2]
	funct7 = dict_of_format[instruction[0]][3]
	
	rd = '{0:05b}'.format(int(instruction[1][1:]))
	rs1 = '{0:05b}'.format(int(instruction[2][1:]))
	rs2 = '{0:05b}'.format(int(instruction[3][1:]))
	machine_code = funct7 + rs2 + rs1 + funct3 + rd + opcode
	return '{0:08X}'.format(int(machine_code, 2))
	

def I_Type(instruction):
	instruction = instruction.split()
	opcode = dict_of_format[instruction[0]][1]
	funct3 = dict_of_format[instruction[0]][2]

	rd = '{0:05b}'.format(int(instruction[1][1:]))
	rs1 = '{0:05b}'.format(int(instruction[2][1:]))
	imm = BitArray(int = int(instruction[3]),length = 12).bin

	machine_code = imm + rs1 + funct3 + rd + opcode
	return '{0:08X}'.format(int(machine_code, 2))


def S_Type(instruction):
	instruction = instruction.split()

	opcode = dict_of_format[instruction[0]][1]
	funct3 = dict_of_format[instruction[0]][2]
	
	rs2 = '{0:05b}'.format(int(instruction[1][1:]))
	rs1 = '{0:05b}'.format(int(instruction[2][1:]))
	imm = BitArray(int = int(instruction[3]),length = 12).bin

	imm1 = imm[7:12]
	imm2 = imm[0:7]

	machine_code = imm2 + rs2 + rs1 + funct3 + imm1 + opcode
	return '{0:08X}'.format(int(machine_code, 2))


def U_Type(instruction):
	instruction = instruction.split()
	opcode = dict_of_format[instruction[0]][1]
	rd = '{0:05b}'.format(int(instruction[1][1:]))
	imm = BitArray(int = int(instruction[2]),length = 32).bin
	imm1 = imm[12:32]
	machine_code = imm1 + rd + opcode
	return '{0:08X}'.format(int(machine_code, 2))


def SB_Type(instruction):
	instruction = instruction.split()
	opcode = dict_of_format[instruction[0]][1]
	funct3 = dict_of_format[instruction[0]][2]
	rs1 = '{0:05b}'.format(int(instruction[1][1:]))
	rs2 = '{0:05b}'.format(int(instruction[2][1:]))
	imm = BitArray(int = int(instruction[3]),length = 13).bin	
	imm1 = imm[0]
	imm2 = imm[1]
	imm3 = imm[2:8]
	imm4 = imm[8:12]
	machine_code = imm1 + imm3 + rs2 + rs1 + funct3 + imm4 + imm2 + opcode
	return '{0:08X}'.format(int(machine_code, 2))


def UJ_Type(instruction):
	instruction = instruction.split()
	opcode = dict_of_format[instruction[0]][1]
	rd = '{0:05b}'.format(int(instruction[1][1:]))
	imm = BitArray(int = int(instruction[2]),length = 32).bin
	imm1 = imm[11]
	imm2 = imm[20]
	imm3 = imm[21:31]
	imm4 = imm[12:20]
	machine_code = imm1 + imm3 + imm2 + imm4 + rd + opcode
	return '{0:08X}'.format(int(machine_code, 2))
