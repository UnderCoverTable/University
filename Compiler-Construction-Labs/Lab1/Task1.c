#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc, char *argv[]){
	FILE *fp;
	char longest_str[100];


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

		if (strlen(buff) > strlen(longest_str)){
			strcpy(longest_str,buff);
		}
		//fputs(buff,stdout);
	}

	printf("Longest line in the file is: %s\n",longest_str);

	//your logic goes here
	return 0;
}


