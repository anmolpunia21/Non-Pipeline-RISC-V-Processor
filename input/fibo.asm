.data

.text
#x5 input
#x7 me output
addi x5 x0 7
addi x6 x0 2
jal x1 FIB
jal x1 EXIT
FIB:
bge x5 x6 REC 
addi x7 x5 0
jalr x0 x1 0
#Handled Base Case
REC:
# Handling Rec. Case
addi x2 x2 -12
sw x1 x2 0
sw x5 x2 4

addi x5 x5 -1
jal x1 FIB


sw x7 x2 8
lw x5 x2 4
addi x5 x5 -2
jal x1 FIB 

lw x13 x2 8
add x7 x13 x7


lw x1 x2 0
lw x5 x2 4
addi x2 x2 12
jalr x0 x1 0

EXIT:
