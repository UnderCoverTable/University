# Program Name: Task 4.asm
# Group Number: 5
# Group Members:
# Taha Hassan, 20-10643
# Muhammad Sameed Gilani, 231488347
# Ahmad Saad, 231461463
##############################

.data
	firstPrompt:	.asciiz "Enter first string: \n"
	secondPrompt: 	.asciiz "Enter second string: \n"
	thirdPrompt:	.asciiz "Enter number of characters to match: \n"
	output:		.asciiz "Output is: \n"
	firstStr:	.space 100
	secondStr:	.space 100				

.text
main:	
	la 	$a0, firstPrompt		# Print first string prompt for user
	li 	$v0, 4
	syscall
	
	la 	$a0, firstStr			# Get first string and store it in firstStr static data from user
	li 	$a1, 100
	li 	$v0, 8
	syscall
	
	la 	$a0, secondPrompt		# Print second string prompt for user
	li 	$v0, 4
	syscall
	
	la 	$a0, secondStr		        # Get second string and store it in secondStr static data from user
	li 	$a1, 100
	li 	$v0, 8
	syscall
	
	la 	$a0, thirdPrompt		# Prompt to get user to integer value
	li 	$v0, 4
	syscall
	
	li 	$v0, 5			        # Get an integer value from user		
	syscall
	
	la 	$a0, firstStr			# Address for first string in $a0
	la 	$a1, secondStr		        # Address for second string in $a1
	move 	$a2, $v0			# Integer value n in $a2
	
	jal 	strncmp
	move 	$t0, $v0			# Temporarily store return value
	
	la 	$a0, output			# Print output message
	li 	$v0, 4
	syscall
	
	move 	$a0, $t0			# Print the output
	li 	$v0, 1
	syscall
	li 	$v0, 10			        # Exit the program
	syscall
	
strncmp:	
	addi 	$sp, $sp, -16		        # Push the stack
	sw 	$ra, 0($sp)			# Store return address and arguments
	sw 	$a0, 4($sp)
	sw 	$a1, 8($sp)
	sw 	$a2, 12($sp)
	li 	$s0, 0			        # Counter for loop

loop: 	beq 	$s0, $a2, equal		        # If the counter reaches n, strings are equal for n characters
	lb 	$t0, 0($a0)			# Load a character from first string
	lb 	$t1, 0($a1)			# Load a character from second string
		
	bne 	$t0, $t1, notequal		# If characters are not equal exit loop
	
	addi 	$a0, $a0, 1			# Increment the addesses
	addi 	$a1, $a1, 1
	add 	$s0, $s0, 1			# Increment the counter
	j loop			
	
equal: 	                                        # Sets return value $v0 to 1 since the strings are equal
	li 	$v0, 1
	j 	done
notequal: 					# Sets return value $v0 to 0 since the strings are not equal.	
	li 	$v0, 0
done:						# Exit the function.
	lw 	$ra, 0($sp)		        # Retrieve return address
	addi 	$sp, $sp, 16		        # Pop the stack
	jr 	$ra
	
	
