# from platform import machine
from bitstring import BitArray

'''
table_for_opcode is a python dictionary (hashtable) for storing the opcodes for various operations
of varying formats and styles, this will be repeatedly used while performing disassembly!
'''

table_for_opcode = {

    "0": {"format": "R"},
    "2": {"format": "J", "operation": "j"},
    "3": {"format": "J", "operation": "jal"},
    "8": {"format": "I", "operation": "addi", "style": 1},
    "9": {"format": "I", "operation": "addiu", "style": 1},
    "d": {"format": "I", "operation": "ori", "style": 1},
    "c": {"format": "I", "operation": "andi", "style": 1},
    "4": {"format": "I", "operation": "beq", "style": 5},
    "5": {"format": "I", "operation": "bne", "style": 5},
    "24": {"format": "I", "operation": "lbu", "style": 4},
    "25": {"format": "I", "operation": "lhu", "style": 4},
    "30": {"format": "I", "operation": "ll", "style": 1},
    "f": {"format": "I", "operation": "lui", "style": 3},
    "23": {"format": "I", "operation": "lw", "style": 4},
    "a": {"format": "I", "operation": "slti", "style": 1},
    "b": {"format": "I", "operation": "sltiu", "style": 1},
    "28": {"format": "I", "operation": "sb", "style": 4},
    "38": {"format": "I", "operation": "sc", "style": 4},
    "29": {"format": "I", "operation": "sh", "style": 4},
    "2b": {"format": "I", "operation": "sw", "style": 4},

}
'''
table_for_funct is a python dictionary (hashtable) for storing the funct for various operations
of varying styles, this will be repeatedly used while performing disassembly 
'''
table_for_funct = {

    "20": {"operation": "add", "style": 0},
    "22": {"operation": "sub", "style": 0},
    "24": {"operation": "and", "style": 0},
    "25": {"operation": "or", "style": 0},
    "27": {"operation": "nor", "style": 0},
    "2a": {"operation": "slt", "style": 0},
    "0": {"operation": "sll", "style": 1},
    "2": {"operation": "srl", "style": 1},
    "8": {"operation": "jr", "style": 2},
    "21": {"operation": "addu", "style": 0},
    "2b": {"operation": "sltu", "style": 0},
    "1a": {"operation": "div", "style": 0},
    "1b": {"operation": "divu", "style": 0},
    "10": {"operation": "mfhi", "style": 0},
    "23": {"operation": "subu", "style": 0},
    "18": {"operation": "mult", "style": 0},
    "19": {"operation": "multu", "style": 0},

}
'''
table_for_registers is a python dictionary (hashtable) for storing various registers!
'''
table_for_registers = {
    0: "$zero",
    1: "$at",
    2: "$v0",
    3: "$v1",
    4: "$a0",
    5: "$a1",
    6: "$a2",
    7: "$a3",
    8: "$t0",
    9: "$t1",
    10: "$t2",
    11: "$t3",
    12: "$t4",
    13: "$t5",
    14: "$t6",
    15: "$t7",
    16: "$s0",
    17: "$s1",
    18: "$s2",
    19: "$s3",
    20: "$s4",
    21: "$s5",
    22: "$s6",
    23: "$s7",
    24: "$t8",
    25: "$t9",
    26: "$k0",
    27: "$k1",
    28: "$gp",
    29: "$sp",
    30: "$fp",
    31: "$ra",
}

#location of input machine code file
# machine_code_input_file = ".\\test_cases_disassembler\\test_j_type.txt"
# #reading the contents of the machine code file and storing it in a variable
# machine_code_input_file = open(machine_code_input_file, 'r')
# initial_address ='0x0' #setting the initial address
# initial_address = int(initial_address,16) #converting the initial address to int
# PC = initial_address #initialize PC
# instruction_list = [] #will consists of all the instructions
# addrList = [] #will consist list of addresses!
# addrTable = {} #hashtable containing addresses as keys and labels as values

# #helper function for converting hexadecimal to binary
# def htob(hex_str, n_bits):
#     return bin(int(hex_str, 16))[2:].zfill(n_bits)

# #helper function for converting decimal to binary
# def dtob(dec, n_bits):
#     if int(dec) < 0:
#         dec = int(dec)
#         b = BitArray(int=dec,length=n_bits)
#         return b.bin
#     else:
#         return bin(int(dec))[2:].zfill(n_bits)

# #helper function for converting binary to decimal
# def btod(bin_str, n_bits):
#     sign_bit = bin_str[0]
#     if sign_bit is '0':
#         return int(bin_str,2)
#     elif sign_bit is '1':
#         to_sub = int(bin_str[1:],2)
#         dec = (2**(n_bits-1)) - to_sub
#         return -1*dec

# '''
# Now, we will read the machine code which is stored in the variable
# '''
# for line in machine_code_input_file:
#     #first, we will extract the opcode from the machine code by reading the first 6 bits
#     opcode = hex(int(line[0:6],2))[2:]
#     #next, we will extract the format and operation from table_for_opcode 
#     data = table_for_opcode[opcode]
#     PC += 4
    
#     # R format types will be analysed here!
#     if data['format'] is 'R':
#         rs = table_for_registers[int(line[6:11],2)] #extracting rs register from table_for_registers
#         rt = table_for_registers[int(line[11:16],2)] #extracting rt register from table_for_registers
#         rd = table_for_registers[int(line[16:21],2)] #extracting rd register from table_for_registers
#         shamt = int(line[21:26],2) #shift 
#         funct = hex(int(line[26:32],2))[2:] #funct
#         operation = table_for_funct[funct]['operation'] #operation
#         style = table_for_funct[funct]['style'] #style format for the operation
        
#         #according to the style instruction will be set!
#         if style is 0:
#             instruction = [operation + ' ' + rd + ', ' + rs + ', ' + rt, None]
#         if style is 1:
#             instruction = [operation + ' ' + rd + ', ' + rt + ', ' + str(shamt), None]
#         if style is 2:
#             instruction = [operation + ' ' + rs, None] 

#     # I format types will be analyzed here!       
#     if data['format'] is 'I':
#         operation =  data['operation'] #operation
#         style = data['style'] #style format for the operation
#         rs = table_for_registers[int(line[6:11],2)] #extracting the rs register from table_for_registers
#         rt = table_for_registers[int(line[11:16],2)] #extracting the rt register from table_for_registers
#         imm = str(btod(line[16:],16)) #immediate value
        
#         #according to the style instruction will be set!
#         if style is 1:
#             instruction = [operation + ' ' + rt + ', ' + rs + ', ' + imm, None]
#         if style is 3:
#             instruction = [operation + ' ' + rt + ', ' + imm, None]
#         if style is 4:
#             instruction = [operation + ' ' + rt + ', ' + imm + '(' + rs + ')',None]
#         if style is 5:
#             address =  int(imm)*4
#             #adding the address to the list of addresses
#             if address not in addrList:
#                 addrList.append(address)
#             instruction = [operation + ' ' + rs + ', ' + rt + ', ' , address]
    
#     # J format types will be analyzed here!
#     if data['format'] is 'J':
#         operation = data['operation'] #operation
#         addr = int(line[6:],2) << 2 #shifts address by 2
#         addr = dtob(addr,28) #return it to binary form
#         addr = dtob(PC,32)[0:4] + addr #concatenate 28 bits of address and the 4 MSBs of PC
#         addr = int(addr,2) #converting to decimal again
        
#         #adding the address to the list of addresses
#         if addr not in addrList:
#             addrList.append(addr)
#         instruction = [operation + ' ' , addr]

#     #adding the instruction to the list of instructions!
#     instruction_list.append(instruction)

# '''
# Once we have the addresses we sort them so as to disassemble them in the correct order!
# '''
# addrList.sort()

# #formulating the address table
# i = 1
# for address in addrTable:
#     addrTable[address] = 'X%d'%i
#     i += 1

# assembly_file = open('.\\disassembled.txt','w') #opening the output file

# line_number = 0 
# for instruction in instruction_list:
#     #setting the value of instruction address    
#     instruction_addr = initial_address + line_number

#     #once this is done we will write the contents to the output file
#     if addrTable.get(instruction_addr) is not None:
#         label = addrTable.get(instruction_addr)
#     else:
#         label = ''
#     if instruction[1] is None:
#         if label is '':
#             assembly_file.write(instruction[0] + '\n')
#         else:
#             # print(label + ': ' + instruction[0])
#             assembly_file.write(instruction[0] + '\n')
#     else:
#         if label is '':
#             # print(instruction[0] + str(instruction[1]))
#             assembly_file.write(instruction[0] + str(instruction[1]) + '\n')
#         else:
#             # print(label + ': ' + instruction[0] + addrTable[instruction[1]])
#             assembly_file.write( instruction[0] + addrTable[instruction[1]] + '\n')
#     line_number += 4        

# assembly_file.close()

def disassemblercode(text,add):
    add = str(add)
    machine_code_input_file = text.split('\n')

    initial_address = add #setting the initial address
    initial_address = int(initial_address,16) #converting the initial address to int
    PC = initial_address #initialize PC
    instruction_list = [] #will consists of all the instructions
    addrList = [] #will consist list of addresses!
    addrTable = {} #hashtable containing addresses as keys and labels as values

    #helper function for converting hexadecimal to binary
    def htob(hex_str, n_bits):
        return bin(int(hex_str, 16))[2:].zfill(n_bits)

    #helper function for converting decimal to binary
    def dtob(dec, n_bits):
        if int(dec) < 0:
            dec = int(dec)
            b = BitArray(int=dec,length=n_bits)
            return b.bin
        else:
            return bin(int(dec))[2:].zfill(n_bits)

    #helper function for converting binary to decimal
    def btod(bin_str, n_bits):
        sign_bit = bin_str[0]
        if sign_bit is '0':
            return int(bin_str,2)
        elif sign_bit is '1':
            to_sub = int(bin_str[1:],2)
            dec = (2**(n_bits-1)) - to_sub
            return -1*dec

    '''
    Now, we will read the machine code which is stored in the variable
    '''
    for line in machine_code_input_file:
        if(line==""): 
            continue
        #first, we will extract the opcode from the machine code by reading the first 6 bits
        opcode = hex(int(line[0:6],2))[2:]
        #next, we will extract the format and operation from table_for_opcode 
        data = table_for_opcode[opcode]
        PC += 4
        
        # R format types will be analysed here!
        if data['format'] is 'R':
            rs = table_for_registers[int(line[6:11],2)] #extracting rs register from table_for_registers
            rt = table_for_registers[int(line[11:16],2)] #extracting rt register from table_for_registers
            rd = table_for_registers[int(line[16:21],2)] #extracting rd register from table_for_registers
            shamt = int(line[21:26],2) #shift 
            funct = hex(int(line[26:32],2))[2:] #funct
            operation = table_for_funct[funct]['operation'] #operation
            style = table_for_funct[funct]['style'] #style format for the operation
            
            #according to the style instruction will be set!
            if style is 0:
                instruction = [operation + ' ' + rd + ', ' + rs + ', ' + rt, None]
            if style is 1:
                instruction = [operation + ' ' + rd + ', ' + rt + ', ' + str(shamt), None]
            if style is 2:
                instruction = [operation + ' ' + rs, None] 

        # I format types will be analyzed here!       
        if data['format'] is 'I':
            operation =  data['operation'] #operation
            style = data['style'] #style format for the operation
            rs = table_for_registers[int(line[6:11],2)] #extracting the rs register from table_for_registers
            rt = table_for_registers[int(line[11:16],2)] #extracting the rt register from table_for_registers
            imm = str(btod(line[16:],16)) #immediate value
            
            #according to the style instruction will be set!
            if style is 1:
                instruction = [operation + ' ' + rt + ', ' + rs + ', ' + imm, None]
            if style is 3:
                instruction = [operation + ' ' + rt + ', ' + imm, None]
            if style is 4:
                instruction = [operation + ' ' + rt + ', ' + imm + '(' + rs + ')',None]
            if style is 5:
                address =  int(imm)*4
                #adding the address to the list of addresses
                if address not in addrList:
                    addrList.append(address)
                instruction = [operation + ' ' + rs + ', ' + rt + ', ' , address]
        
        # J format types will be analyzed here!
        if data['format'] is 'J':
            operation = data['operation'] #operation
            addr = int(line[6:],2) << 2 #shifts address by 2
            addr = dtob(addr,28) #return it to binary form
            addr = dtob(PC,32)[0:4] + addr #concatenate 28 bits of address and the 4 MSBs of PC
            addr = int(addr,2) #converting to decimal again
            
            #adding the address to the list of addresses
            if addr not in addrList:
                addrList.append(addr)
            instruction = [operation + ' ' , addr]

        #adding the instruction to the list of instructions!
        instruction_list.append(instruction)

    '''
    Once we have the addresses we sort them so as to disassemble them in the correct order!
    '''
    addrList.sort()

    #formulating the address table
    i = 1
    for address in addrTable:
        addrTable[address] = 'X%d'%i
        i += 1

    return_string = ""
    line_number = 0 
    for instruction in instruction_list:
        #setting the value of instruction address    
        instruction_addr = initial_address + line_number

        #once this is done we will write the contents to the output file
        if addrTable.get(instruction_addr) is not None:
            label = addrTable.get(instruction_addr)
        else:
            label = ''
        if instruction[1] is None:
            if label is '':
                return_string += instruction[0] + '\n'
            else:
                return_string += instruction[0] + '\n'
        else:
            if label is '':
                # print(instruction[0] + str(instruction[1]))
                return_string += instruction[0] + str(instruction[1]) + '\n'
            else:
                return_string += instruction[0] + addrTable[instruction[1]] +'\n'
        line_number += 4        
    return return_string