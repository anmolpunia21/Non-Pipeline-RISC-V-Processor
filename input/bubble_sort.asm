.text

addi x4 x0 6
# loading 'length' number of numbers in the array
addi x15, x0, 84
sw x15, x3 0
addi x15, x0, -78
sw x15, x3 4
addi x15, x0, 788
sw x15, x3 8
addi x15, x0, -89
sw x15, x3 12
addi x15, x0, 75
sw x15, x3 16
addi x15, x0, -7
sw x15, x3 20
addi x22 x0 2

jal x1 BubbleSort
jal x0 Exit_Beyond
BubbleSort:
addi x2, x2, -20
sw x8, x2 16
sw x7, x2 12
sw x6, x2 8
sw x5, x2 4
sw x1, x2 0
addi x5, x0, 0					# int i
addi x6, x4, -1				# x6 = n-1

OuterLoop:
bge, x5, x6, Exit_Outer			# exit outer loop if i >= n-1
addi x8, x0, 0						# int j
sub x9, x6, x5					# x9 = n-1-i

InnerLoop:
bge x8, x9, Exit_inner
addi x10, x8, 0
sll x10, x10, x22			# we now have the offset
add x10, x10, x3
lw x11, x10 0				# array[i]
lw x12, x10 4				# array[i+1]
bge x12, x11, continue_inner

swap:
sw x12, x10 0
sw x11, x10 4		# swap array[i] and array[i+1]

continue_inner:
addi x8, x8, 1			# increment j
beq x0, x0, InnerLoop

Exit_inner:
addi x5, x5, 1			# increment i
beq x0, x0, OuterLoop

Exit_Outer:
lw x1, x2	0			# load x1 from stack
lw x5, x2 4
lw x6, x2 8
lw x7, x2 12
lw x8  x2 16
addi x2, x2, 20				# pop from stack
jalr x0, x1 0				# jump to the caller

Exit_Beyond:
