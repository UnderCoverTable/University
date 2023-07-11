# Program Name: Task 1.asm
# Group Number: 5
# Group Members:
# Taha Hassan, 20-10643
# Muhammad Sameed Gilani, 231488347
# Ahmad Saad, 231461463
##############################

.data
prompt: .asciiz"Enter String: \n"
inputstring: .space 1024
outputmsg: .asciiz "Length of string is: "
.text
#printing prompt
li $v0,4 
la $a0,prompt
syscall
#getting the user input for the string
li $v0, 8
la $a0, inputstring
li $a1, 1024
syscall
#setting the counter
li $t0, -1
#getting the string into a temporary register
la $t1, inputstring
#calculating the length of the string
callength:
lb $t2, 0($t1)
beqz $t2, label #check for null character
add $t1, $t1, 1  #incrementing the string pointer
add $t0, $t0, 1   #incrementing the counter
j callength    #back to the top of loop


label:
#displaying the output message
li $v0,4
la $a0, outputmsg
syscall
#final result
li $v0, 1
move $a0, $t0
syscall
#graceful exit
li $v0,10
syscall 