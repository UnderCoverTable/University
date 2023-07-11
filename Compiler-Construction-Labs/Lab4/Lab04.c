#include <stdio.h>
#include <stdlib.h>

// 231488347
// 231453415

void removeUnnecessarySpaces(char*);

int main(int argc, char *argv[]){
    

    if(argc != 2){
	printf("This program needs a text file as argument\n");
	exit(0);
	}

	removeUnnecessarySpaces(argv[1]);

	return 0;

}

void removeUnnecessarySpaces(char *str){

    int index = 0;
    char* buff = (char*) malloc(sizeof(char)*1000); // Allocates memory of 2000 bytes 
     

    while ( str[index] != ';' || str[index] != '\0'){

        if (index == 0 && str[index] == ' '){
            index++;
        }

        while(index >= 0 && str[index-1] == ' ' && str[index] == ' ' ){
            index++;
        }
        while(index>=0 && str[index] == ' ' ){

        }
        

        index++;
    }




}