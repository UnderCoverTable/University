#include <stdio.h>
#include <stdlib.h>



int get_length(char *);
void cpy_strings(char *destination, char *source);
int main(int argc, char *argv[]){

	FILE *fp;
	char longest_str[100] = "ee\n";

	//check number of args
	if(argc != 2){
		printf("This program needs a text file as argument\n");
		exit(0);
	}	

	fp = fopen(argv[1],"r");

	if (fp == NULL){
		printf("Error opening file");
		exit(0);
	}


	char* buff = (char*) malloc(sizeof(char)*1000);

	while(fgets(buff,1000,fp) != NULL){
		//printf("%d\n",get_length(longest_str));


		if (get_length(buff) > get_length(longest_str)){
			cpy_strings(longest_str,buff);
		}
	}

	printf("Longest line in the file is: %s\n",longest_str);


	//your logic goes here
	return 0;

}



int get_length(char *s){
	
	int len = 0;
	
	while(*s != '\n'){
		len ++;
		s++;
	}
	return len;
}


void cpy_strings(char *destination, char *source){

	while (*source != '\0'){
		*destination = *source;
	    destination++;
	    source++;
	}
   
}
