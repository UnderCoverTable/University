#include <stdio.h>
#include <stdlib.h>

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
    int valid = 0;

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
        nextState = 2;
        goto Q2;
    }
    else if(currC == 'b'){
        nextState = 1;
        goto Q1;
    }
    else{
        goto terminate;
    }

    terminate:
        printf("Invalid character %c at Q%d\n terminating process\n",currC,source);
        return 0;
    
    validate:
        if(valid == 1){
            printf("String %s is valid\n",buff);
            return 0;
        }
        if(valid == 0){
            printf("String %s is invalid\n",buff);
            return 0;

        }
    
    
	

    Q1:
    printf("Recvied %c at state Q%d ---- Moving to state Q%d\n",currC,source,nextState);
    source = 1;
    currC = fgetc(fp);

    if(currC == '$'){
        goto validate;
    }
    if(currC != 'a' && currC != 'b'){
        goto terminate;
    }
    else{
        if(currC == 'a'){
            nextState = 2;
            goto Q2;
        }
        if(currC == 'b'){
            nextState = 3;
            goto Q3;
        }
    }

    

    Q2:
    printf("Recvied %c at state Q%d ---- Moving to state Q%d\n",currC,source,nextState);
    source = 2;

    currC = fgetc(fp);

    if(currC == '$'){
        goto validate;
    }
    if(currC != 'a' && currC != 'b'){
        goto terminate;
    }
    
    else{
        if(currC == 'a'){
            nextState = 4;
            goto Q4;
        }
        if(currC == 'b'){
            nextState = 1;
            goto Q1;
        }
    }
     

    Q3:
    printf("Recvied %c at state Q%d ---- Moving to state Q%d\n",currC,source,nextState);
    source = 3;

    currC = fgetc(fp);

    if(currC == '$'){
        valid = 1;
        goto validate;
    }
    if(currC != 'a' && currC != 'b'){
        goto terminate;
    }
    
    else{
        if(currC == 'a'){
            nextState = 2;
            goto Q2;
        }
        if(currC == 'b'){
            nextState = 3;
            goto Q3;
        }
    }
     

    Q4:
    printf("Recvied %c at state Q%d ---- Moving to state Q%d\n",currC,source,nextState);
    source = 4;

    currC = fgetc(fp);
    if(currC == '$'){
        valid = 1;
        goto validate;
    }
    if(currC != 'a' && currC != 'b'){
        goto terminate;
    }
    
    else{
        if(currC == 'a'){
            nextState = 4;
            goto Q4;
        }
        if(currC == 'b'){
            nextState = 1;
            goto Q1;
        }
    }


	return 0;
}

