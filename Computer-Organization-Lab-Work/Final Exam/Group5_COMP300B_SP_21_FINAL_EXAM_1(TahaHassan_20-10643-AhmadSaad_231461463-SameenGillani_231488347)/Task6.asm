# Program Name: Task 6.asm
# Group Number: 5
# Group Members:
# Taha Hassan, 20-10643
# Muhammad Sameed Gilani, 231488347
# Ahmad Saad, 231461463
##############################

.data
prompt1: .asciiz"Enter String: " 
prompt2: .asciiz"Enter character to find: "
prompt3: .asciiz"\nEnter character to replace: "
prompt4: .asciiz"\nThe find-n-replace results in: "
prompt5: .asciiz"\nCould not find character "
prompt6: .asciiz" in the string."
string: .space 100
char: .space 1
.text
main: 
#printing the string to get input
li $v0,4
la $a0,prompt1
syscall
#reading string
la $a0,string
li $a1, 100
li $v0,8
syscall

#printing string to get character input
li $v0,4
la $a0,prompt2
syscall
li $v0, 12
syscall
sb $v0,char #storing chracter
move $s2,$v0 #moving it to $s2


#printing string to get character to replace with
li $v0,4
la $a0,prompt3
syscall

li $v0,12
syscall
move $t1,$v0 #moving content to $t1

li $t3,0
la $a0,string


label3:
lb $t2,0($a0) #$t2 a character from string
beqz $t2,label1
beq $t2, '\n', label1 #if $t2 null, or $t2=/n goto label1
bne $s2,$t2,label2  #if the string doesnt match go to label2
sb $t1,0($a0)  #replacing character
li $t3,1  #set flag to 1
label2: #for incrementing string address
addi $a0,$a0,1
j label3



label1:
# Print a message  with the replacement results
beqz $t3,label4
li $v0,4
la $a0, prompt4
syscall

li $v0,4
la $a0,string
syscall
j label5

#if the character is not found in the string
label4:
li $v0,4
la $a0, prompt5
syscall
li $v0,4
la $a0, char
syscall
li $v0,4
la $a0, prompt6
syscall
#gracefull exit
label5:
li $v0,10
syscall
