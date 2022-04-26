from pyparsing import *
from bitstring import BitArray

'''
{instructions} is a python dictionary (a hashtable in the classical CS jargon) that stores the various type of instructions
that our program will assemble to machine code.
It consists of 3 formats -> R,I,J
within each format the various instructions are further distinguised on the basis of
funct type; style ,i.e, the syntax of the instruction(s) and opcode!
style summary is as follows:
-> style 0 -> operation register,register,register
-> style 1 -> operation register,register,integer
-> style 2 -> operation register
-> style 3 -> operation register,integer
-> style 4 -> operation register,integer(reg)
-> style 5 -> operation register,register,address
'''

instructions = {

    #R type instructions
    "add": {"format": "R", "opcode": "0", "style": 0, "funct": "20"},
    "addu": {"format": "R", "opcode": "0", "style": 0, "funct": "21"},
    "and": {"format": "R", "opcode": "0", "style": 0, "funct": "24"},
    "jr": {"format": "R", "opcode": "0", "style": 2, "funct": "08"},
    "nor": {"format": "R", "opcode": "0", "style": 0, "funct": "27"},
    "or": {"format": "R", "opcode": "0", "style": 0, "funct": "25"},
    "slt": {"format": "R", "opcode": "0", "style": 0, "funct": "2a"},
    "sltu": {"format": "R", "opcode": "0", "style": 0, "funct": "2b"},
    "sll": {"format": "R", "opcode": "0", "style": 1, "funct": "00"},
    "srl": {"format": "R", "opcode": "0", "style": 1, "funct": "02"},
    "sub": {"format": "R", "opcode": "0", "style": 0, "funct": "22"},
    "subu": {"format": "R", "opcode": "0", "style": 0, "funct": "23"},
    "div": {"format": "R", "opcode": "0", "style": 0, "funct": "1a"},
    "divu": {"format": "R", "opcode": "0", "style": 0, "funct": "1b"},
    "mfhi": {"format": "R", "opcode": "0", "style": 0, "funct": "10"},
    "mult": {"format": "R", "opcode": "0", "style": 0, "funct": "18"},
    "multu": {"format": "R", "opcode": "0", "style": 0, "funct": "19"},

    #I type instructions
    "beq": {"format": "I", "opcode": "4", "style": 5},
    "bne": {"format": "I", "opcode": "5", "style": 5},
    "addi": {"format": "I", "opcode": "8", "style": 1},
    "addiu": {"format": "I", "opcode": "9", "style": 1},
    "andi": {"format": "I", "opcode": "c", "style": 1},
    "lbu": {"format": "I", "opcode": "24", "style": 4},
    "lhu": {"format": "I", "opcode": "25", "style": 4},
    "ll": {"format": "I", "opcode": "30", "style": 1},
    "lui": {"format": "I", "opcode": "f", "style": 3},
    "lw": {"format": "I", "opcode": "23", "style": 4},
    "ori": {"format": "I", "opcode": "d", "style": 1},
    "slti": {"format": "I", "opcode": "a", "style": 1},
    "sb": {"format": "I", "opcode": "28", "style": 4},
    "sc": {"format": "I", "opcode": "38", "style": 4},
    "sh": {"format": "I", "opcode": "29", "style": 4},
    "sw": {"format": "I", "opcode": "2b", "style": 4},
    "sltiu": {"format": "I", "opcode": "b", "style": 1},

    #J type instructions
    "j": {"format": "J", "opcode": "2"},
    "jal": {"format": "J", "opcode": "3"},

}
'''
all the valid instructions are keys of the dictionary 
and will be used for validating the input instructions of our MIPS program!
'''
valid_instructions = instructions.keys()

'''
Next, we will try to declare our operations.
<A>_<#> Here, 'A' corresponds to the instruction format and '#' represents the style 
in which the particular instruction format will be used!
These declarations will be used for setting the parsing rules for our input
MIPS program which will streamline the process of tokenising the various 
lines of instructions that we have to take care of! 
'''
R_0 = []
R_1 = []
R_2 = []
I_1 = []
I_3 = []
I_4 = []
I_5 = []
J = []
for operation in valid_instructions:
    curr_operation = instructions[operation]
    if curr_operation['format']  == 'R':
        if curr_operation['style']  == 0: R_0.append(operation) #all R format with style 0 go in th == list
        if curr_operation['style'] == 1: R_1.append(operation) #all R format with style 1 go in this list
        if curr_operation['style'] == 2: R_2.append(operation) #all R format with style 2 go in this list
        
    if curr_operation['format'] == 'I':
        if curr_operation['style'] == 1: I_1.append(operation) #all I format with style 1 go in this list
        if curr_operation['style'] == 3: I_3.append(operation) #all I format with style 3 go in this list
        if curr_operation['style'] == 4: I_4.append(operation) #all I format with style 4 go in this list
        if curr_operation['style'] == 5: I_5.append(operation) #all I format with style 5 go in this list
    
    if curr_operation['format'] == 'J': J.append(operation) #all J format go in this list


'''
Then, we create a python dictionary [read hashtable] for all the valid registers 
that will be handled by our assembler
'''

#declaration of $zero, $at, $v0, $2, $v1, $gp, $sp, $fp, $ra
registers = {"$zero": 0, "$at": 1, "$v0": 2, "$2": 2, "$v1": 3, '$gp' : 28, '$sp' : 29, '$fp':30, '$ra':31,'': 0}

#declaration of $a0...$a3 registers
for z in range(0,4): registers['$a%d'%z]= z+4

#declaration of $t0...$t7 and $s0...$s7 registers
for z in range(0,8):
    registers['$t%d'%z]= z+8
    registers['$s%d'%z]= z+16

#declaration of $t8,$t9 registers
for z in range(8,10):
    registers['$t%d'%z]= z+24

#declaration of $k0,$k1 registers
for z in range(0,2):
    registers['$k%d'%z]= z+26

#declaration of $0..$30 registers
for z in range(0,31):
    registers['$%d'%z]=z

#valid_registers stores all the valid registers 
valid_registers = list(registers.keys())


'''
Now, we set the parsing rules our MIPS program
First, there will be alphanumeric identifiers
permutation of registers from valid_registers

'''
Identifiers =  Word(alphas+"_",alphanums+"_") #Identifying words, alphanumerics
Register = oneOf(valid_registers) #identifying registers
Comma = Suppress(',') #splitting by ,
Numbers = Combine(Optional('-') + Word(nums)) #identifying numbers
EOL = OneOrMore(LineEnd()) #identifying end of line!

Label = Identifiers.setResultsName("label") + Suppress(":") #Label identifiers
rs_register = Register.setResultsName('rs') #rs register
rt_register = Register.setResultsName('rt') #rt register
rd_register = Register.setResultsName('rd') #rd register
immediate_value = Numbers.setResultsName('imm') #immediate value
Address = Identifiers.setResultsName("address") #Address

#R_format will be used for matching an R type instruction format!
R_format = (oneOf(R_0).setResultsName('operation') + White() + rd_register + Comma + rs_register + Comma + rt_register) ^\
           (oneOf(R_1).setResultsName('operation') + White() + rd_register + Comma + rt_register + Comma + Numbers.setResultsName('shamt')) ^\
           (oneOf(R_2).setResultsName('operation') + White() + rs_register)

#I_format will be used for matching an I type instruction format
I_format = (oneOf(I_1).setResultsName('operation') + White() + rt_register + Comma + rs_register + Comma + immediate_value) ^\
           (oneOf(I_3).setResultsName('operation') + White() + rt_register + Comma + immediate_value) ^\
           (oneOf(I_4).setResultsName('operation') + White() + rt_register + Comma + immediate_value + Suppress('(') + rs_register + Suppress(')')) ^\
           (oneOf(I_5).setResultsName('operation') + White() + rs_register + Comma + rt_register + Comma + Address)

#J_format will be used for matching a J type instruction format
J_format = oneOf(J).setResultsName('operation') + White() + Address

#instruction_structure is used as a general matching format
instruction_structure =   ((Label) + (R_format ^ I_format ^ J_format)) ^\
                (Label) ^ (R_format ^ I_format ^ J_format) ^ EOL.setResultsName('EOL')

#ignore the comments!
instruction_structure.ignore(pythonStyleComment)

def assemblercode(text,add):
    add = str(add)
    assembly_file_to_read = text.split('\n')
    init_address = add 

    mem = [] #used for storing the instructions in memory
    lbl = {} #label
    dict ={} #temporary dictionary
    exe = ["j","jal",'beq','bne'] #for handling branch instructions
    cnt =0
    address_of_line = int(init_address,16) #setting the line address

    #parsing the input MIPS file 
    for line in assembly_file_to_read:
        templine = line.split(" ")
        if(templine[0] in exe):
            dict[cnt] = templine
            mem.append(cnt)
            cnt+=1
            continue

        instruction_curr = instruction_structure.parseString(line)
        
        #current line is empty -> skip to next line
        if len(instruction_curr) == 0: 
            continue
        #current line is a newline character -> skip to next line
        if instruction_curr[0] == '\n': 
            continue
        #append the instruction in memory to be analyzed later!
        mem.append(instruction_curr) 
        #labelling the current instruction
        if instruction_curr.label  !=  '':
            if instruction_curr.operation  !=  '': 
                lbl[instruction_curr.label] = address_of_line
            else :  
                lbl[instruction_curr.label] = address_of_line
                continue
        address_of_line += 4 
    # helper function for converting hexadecimal string to binary
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
    PC = int(init_address,16) #program counter
    #analysing the instructions in memory!
    return_string = "" # assemble code in here
    for instruction in mem:
        #handling branch instructions!
        if(type(instruction)==int):
            temp = dict[instruction]
            # J JAL BEQ BNE are handle differently
            # for J and JAL
            # the machine code is formed using the operation opcode which  is ^ bits and
            # rest 26 bits is the address location divided by 4 bits

            if(temp[0]=='jal' or temp[0]=='j'):
                operation = instructions[temp[0]]
                opcode = operation['opcode']
                addr = int(temp[1])
                addr = dtob(addr,32)
                addr = addr[4:]
                addr = int(addr,2)
                addr = addr//4
                addr = dtob(addr,26)
                machine_code_instr = htob(opcode,6) + addr
                return_string += machine_code_instr+"\n"
                PC += 4
            # for beq bne
            # machine code is formed from opcode(6) rs(5) rt(5) imm(16)
            if(temp[0]=='beq' or temp[0]=='bne'):
                operation = instructions[temp[0]]
                opcode = operation['opcode']
                rs = registers[temp[1][:-1]]
                rt = registers[temp[2][:-1]]
                machine_code_instr = htob(opcode,6) + dtob(rs,5) + dtob(rt,5) + dtob(int(temp[3])//4,16)
                return_string += machine_code_instr+"\n"

                PC += 4
            continue
        
        if instruction.operation == '':
            continue
        op = instructions[instruction.operation]
        PC += 4
        
        if op['format'] == 'R':
            opcode = op['opcode']
            funct = op['funct']
            if instruction.shamt  !=  '': shamt = instruction.shamt
            else: shamt = 0
            rs_code = registers[instruction.rs]
            rt_code = registers[instruction.rt]
            rd_code = registers[instruction.rd]
            #machine code is formed from opcode(6 bits) rs(5 bits) rt(5 bits) rd(5 bits) shift(5 bits) funct(6 bits)
            machine_code_instr = htob(opcode,6) + dtob(rs_code,5) + dtob(rt_code,5) + dtob(rd_code,5) +\
                        dtob(shamt,5) + htob(funct,6)
            return_string += machine_code_instr+"\n"


            
        if op['format'] == 'I':
            opcode = op['opcode']
            rs = registers[instruction.rs]
            rt = registers[instruction.rt]
            if instruction.imm  !=  '': imm = instruction.imm
            else:
                addr = lbl[instruction.address]
                imm = (addr - PC)/4
            #machine code is generated by opcode(6 bits) rs(5 bits) rt(5 bits) imm(16 bits)
            machine_code_instr = htob(opcode,6) + dtob(rs,5) + dtob(rt,5) + dtob(imm,16)
            return_string += machine_code_instr+"\n"

            
        if op['format'] == 'J':
            opcode = op['opcode']
            addr = lbl[instruction.address]
            addr = dtob(addr,32)
            addr = addr[4:]
            addr = int(addr,2)
            addr = addr/4
            addr = dtob(addr,26)
            #machine code is generated by opcode(6 bits) addr(26 bits)
            machine_code_instr = htob(opcode,6) + addr
            return_string += machine_code_instr+"\n"

    return return_string