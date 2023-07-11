
int main(int argc, char *argv[]){
    FILE *fp;
    

    if(argc != 3){
	printf("This program needs a text file as argument\n");
	exit(0);
	}

	fp = fopen(argv[1],"r");
    char count_char = *argv[2]; // The character thats occurences are to be counted

	if (fp == NULL){ // Prints an error and exits if file doesnt open
		printf("Error opening file");
		exit(0);
	}

    char* buff = (char*) malloc(sizeof(char)*1000); // Allocates memory of 2000 bytes 

    //buff = fgetc(fp);
    char store_c = ' ';     // This variable stores every character that is read from the file
    int counter = 0;        // Stores the occurences of the user input character
    int len = 0;            // Used to index buff, the memory allocated earlier
    int line_num = 1;       // Unused. 
    int num_of_lines = 0;   // Stores the number of lines in the file
    int num_of_c_in_line = 0;   // Stores the number of characters in each line

    int num_of_c_in_line_arr [10];  // The number of characters from the variable,num_of_c_in_line, is stored in this array
    int i = 0;

    while(store_c != EOF){  // Loop runs while the file doesnt end
        //buff[len] = line_num;
        //len++;
        
        store_c = fgetc(fp);    // Gets each character from the file
        num_of_c_in_line ++;    // Increments number of chacracters in line

        if (store_c == count_char){
            counter ++;         // Incremenets character occurunces, if the read character is the users input char
        }
        if (store_c == '\n'){   // if a new line character is read
            num_of_lines++;     // Increments number of lines in the file
            num_of_c_in_line_arr[i] = num_of_c_in_line-1;   // As we have read newline, we store the number of char in that line, 
            num_of_c_in_line = 0;                           // then we reset the counter that stores number of char in line read.
            i++;
        }
        
        buff[len] = store_c; // Adds the character read this iteration to the memory allocated through buff
        len ++;              // Increments len to store the next character

    }

    for (int i = 0, j = 1; i<len-1;i++){
        if(i ==0 || buff[i-1] == '\n'){
            printf("\n%d. ",j);
            j++;
        }
        if(buff[i] != '\n'){
            printf("%c",buff[i]);
        
        }

    }
   // printf(buff,stdout);
    
    printf("\nNumber of lines in file:%d\n",num_of_lines); // Prints number of lines in the file

    int e = 0;
    while (num_of_c_in_line_arr[e] != 0){ // Iterates through the array and prints the num of char in each line
            printf("Number of charaters in line No.%d: %d\n",e+1,num_of_c_in_line_arr[e]); 
            e++; 
    }
    printf("Character '%c' found %d times in file.\n",count_char,counter ); // Prints the number of occurunces of user input char
    
    return 0;

