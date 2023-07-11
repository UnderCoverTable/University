#include <stdio.h>
#include <stdlib.h>

// 231488347
// 231453415

void removeBlankLines(char*);

int main(int argc, char *argv[]){
    

    if(argc != 2){
	printf("This program needs a text file as argument\n");
	exit(0);
	}

	removeBlankLines(argv[1]);

	return 0;

}

void removeBlankLines(char *fileName){
	FILE *fp;

	char read_char = ' ';
	int len = 0;
	int len1 = 0;

	fp = fopen(fileName,"r");
	if (fp == NULL){ // Prints an error and exits if file doesnt open
		printf("Error opening file");
		exit(0);
	}


	char* buff = (char*) malloc(sizeof(char)*1000); // Allocates memory of 2000 bytes 
	char* buff1 = (char*) malloc(sizeof(char)*1000); // Allocates memory of 2000 bytes 


	while (read_char != EOF){
		read_char = fgetc(fp);

		buff[len] = read_char;
		len ++;

		}
		
	buff[len] = '*';

	len = 0;
	len1 = 0;
	read_char = ' ';
	while (read_char != '*'){
		
		read_char = buff[len]; 
		buff1[len1] = read_char;
		len++;
		len1++;

		//read_char = buff[len]; (read_char == '\n' && buff[len+1] == '\t') || 

		while(buff[len] == '\n' || buff[len] == '\t' ||buff[len] == ' ') {
			len++;
			
		}

		

		
	}
	
		

		
	
	

	
	
	//printf(buff,stdout);
	
	printf(buff1,stdout);
		

} 