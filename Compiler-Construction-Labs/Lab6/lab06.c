#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
    FILE *fp;

	if(argc != 2)
	{
		printf("Need to have a file name in the arguments of this program\n");
		exit(0);
	}

    fp = fopen(argv[1],"r");
    
    if (fp == NULL){ // Prints an error and exits if file doesnt open
		printf("Error opening file");
		exit(0);
	}

    char currC = ' ';
    int source = 0; 
    int nextState = 0;

    char* buff = (char*) malloc(sizeof(char)*100); // Allocates memory of 2000 bytes 
    int i = 0;
    while(currC != '$'){
        currC=fgetc(fp);
        buff[i] = currC;
        i++;
    }
    printf("Input String is: %s\n",buff);
    printf("State Transitions are shown below: \n\n");

    currC = ' ';
    rewind(fp);
    currC = fgetc(fp);

    if(currC == 'a'){
        goto Q1;
    }
    if(currC == 'b'){
        goto Q2;



    }
    
	

    Q1:
    if(currC != 'a' && currC != 'b'){
        printf("Recieved unknown character %c on state Q%d\n",currC,source);
        printf("Terminating Process");
        return 0;
    }
    if(currC == 'a') nextState = 2;
    if(currC == 'b') nextState = 3;

    printf("Recieved %c on state Q%d --- Moving to state Q%d\n",currC,source,nextState);
    source = nextState;
    currC = fgetc(fp);
  
    if(currC == '$'){
        printf("\nEnd of String(%s).\nString Accepted",buff);
        return 0;
    }
    if(nextState == 2) goto Q2;
    if(nextState == 3) goto Q3;

    Q2:
     if(currC != 'a' && currC != 'b'){
        printf("Recieved unknown character %c on state Q%d\n",currC,source);
        printf("Terminating Process");
        return 0;
    }
    if(currC == 'a') nextState = 4;
    if(currC == 'b') nextState = 1;
    printf("Recieved %c on state Q%d --- Moving to state Q%d\n",currC,source,nextState);
    source = nextState;
    currC = fgetc(fp);
    if(currC == '$'){
        printf("\nEnd of String(%s).\nString Accepted",buff);
        return 0;
    }
    if(nextState == 1) goto Q1;
    if(nextState == 4) goto Q4;

    Q3:
     if(currC != 'a' && currC != 'b'){
        printf("Recieved unknown character %c on state Q%d\n",currC,source);
        printf("Terminating Process");
        return 0;
    }
    if(currC == 'a') nextState = 2;
    if(currC == 'b') nextState = 3;
    printf("Recieved %c on state Q%d --- Moving to state Q%d\n",currC,source,nextState);
    source = nextState;
    currC = fgetc(fp);
    
    if(currC == '$'){
        printf("\nEnd of String(%s).\nString Rejected",buff);
        return 0;
    }
    if(nextState == 2) goto Q2;
    if(nextState == 3) goto Q3;

    Q4:
     if(currC != 'a' && currC != 'b'){
        printf("Recieved unknown character %c on state Q%d\n",currC,source);
        printf("Terminating Process");
        return 0;
    }
    if(currC == 'a') nextState = 4;
    if(currC == 'b') nextState = 1;
    printf("Recieved %c on state Q%d --- Moving to state Q%d\n",currC,source,nextState);
    source = nextState;

    currC = fgetc(fp);
    if(currC == '$'){
        printf("\nEnd of String(%s).\nString Rejected",buff);
        return 0;
    }
    if(nextState == 4) goto Q4;
    if(nextState == 1) goto Q1;

    




	return 0;
}
