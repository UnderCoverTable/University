# Program Name: Task 5.asm
# Group Number: 5
# Group Members:
# Taha Hassan, 20-10643
# Muhammad Sameed Gilani, 231488347
# Ahmad Saad, 231461463
##############################

.data 
	prompt: 	.asciiz "Enter String: "
        promptTwo: 	.asciiz "Enter character: "
        nextLine: 	.asciiz "\n"
        occurances: 	.asciiz "Frequency of occurrence of given character: "
    	string:      	.space 100                                # Maximum string size the program accepts is 100
.text
main: 
    	li 	$v0, 4                                            # Asking user for input
    	la 	$a0, prompt
    	syscall
    	
    	la 	$a0, string                             	  # Here the string is being read and stored
    	li 	$a1, 100                                
    	li 	$v0, 8                                  
    	syscall  
    
    	move 	$a3, $a0                                          # Here I move the string to a different register
    	li 	$v0, 4                                            # I also ask the user for a character input
    	la 	$a0, promptTwo
    	syscall
                   
    	li 	$v0, 12                                           # Here I read and store the character
    	syscall                                    
    	
    	move 	$s2, $v0                                          # I store the character in register $s2
    	li 	$s1, 100                                          # $s1 will be upper bound for my loop as it is the string length       
    	li  	$t4, 0                                            # This is increment variable for character repitition count
    	li  	$t0, 0                                            # This is the index being observed
    	bge 	$t0, $s1, finalPrint                              # This is the break condition

increment:                        
    	lb  	$s0,($a3)                                         # Register $s0 reads every index of the string one by one 
    	bne 	$s0, $s2, noIncrement                             # If the character and the index do not match, there is no increment            
    	add 	$t4, $t4, 1                                       # If they do match, 1 is added to the increment variable  
    
noIncrement:
    	addiu 	$a3, $a3, 1                                       # Index for the string is incremented here
    	beq 	$s0, 0, finalPrint                                # finalPrint function is called if the string has ended
    	j  	increment                                         # Otherwise, increment function is recalled
    
finalPrint:                                                                                                 
    	li 	$v0, 4				                  # Moving to next line
    	la 	$a0, nextLine
    	syscall
    
    	li 	$v0, 4                                            # Printing appropriate output prompt
    	la 	$a0, occurances
    	syscall                   
    	
    	li 	$v0, 1                                            # Printing the amount of occurances of character as an integer      
    	move 	$a0, $t4                                          # Moving the count from $t4 to $a0
    	syscall                                      
    
    	li 	$v0, 10                                           # Graceful exit
    	syscall                                    
