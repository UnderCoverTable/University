#include <stdio.h>
#include <string.h>
int S();
int X();
int Z();
char expr[100];
int count,l,countRestore;

int main()
{
    count = 0;
    printf("\nRecursive descent parsing for the following grammar\n");
    printf("\nE->iE'\nE'->+iE'| @\n");
    printf("\nEnter the string to be checked:");
    
    fgets(expr,100,stdin);
    if(S())
    {
        //count++;
        if(expr[count]=='$'){
           // printf("%c",expr[count]);
            printf("\nString is accepted");
        }
        else{
            //printf("%c",expr[count-2]);
            printf("\nString is not accepted");

        }
}
else{
   // printf("%c",expr[count]);

    printf("\nString not accepted");
}
return 0;
}


int S(){

    if(expr[count] == 'r')
    {
     count++;
     //printf("This is X %d\n",X());
     //printf("THIS IS Z %d",Z());
    int valX = X();
    int valZ = Z();
    //printf("%d",valX);
    //printf("%d",valZ);

     if(valX||valZ){
        count++;
        if(expr[count] == 'd'){
            count++;
            return 1;
        }
        else{
            return 0;
        }
     }
       

    }

}

int X(){
    //count++;
    if(expr[count] == 'o'){
        count++;
        if(expr[count] == 'a'){
            return 1;
        }
        else{
            count--;
            return 0;
        }
    }

    if(expr[count] == 'e'){
        count++;
        if(expr[count] == 'a'){
            return 1;
        }
        else{
            count--;
            return 0;
        }
    }

}

int Z(){
    //count++;
    //printf("after Z   %c",expr[count]);

    if(expr[count] == 'a'){
        count++;
        if(expr[count] == 'i'){
            return 1;
        }
        else{
            count --;
            return 0;
        }
    }
    else{
        return 0;
    }
}


