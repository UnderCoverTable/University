#include <stdio.h>
#include <unistd.h>
#include <wait.h>
#include <time.h>
#include <math.h>

double math_delay(){
    int i;
    double x = 50;
    double y = 19;

    for(i=0; i<=100000000; i++)
    {
      x = log(x);
      y = sqrt(x);
      x = x + y;
      y = y + x;
      x = log(x*y);
    }
    return x;
}

int main() {

    pid_t pid;
    int i;
    double start_time;
    double end_time;
    double run_time;
    
    for(i = 1; i<=4; i++)
    {
    pid = fork();

    
    if (pid>0){
     
	printf("\nIM PARENT  %d\n",getpid());
        start_time = clock();

        math_delay();
        wait(NULL);

        end_time = clock();
        run_time = (end_time - start_time)/CLOCKS_PER_SEC;
        printf("\nRUNTIME: %f - PARENT PID: %d\n",run_time,getpid());
      }
        
    else{

	printf("\nIM PARENT %d - My CHILD is:  %d\n",getppid(), getpid());
        start_time = clock();
       
        math_delay();
        wait(NULL);

        end_time = clock();
        run_time = (end_time - start_time)/CLOCKS_PER_SEC;
        printf("\nRUNTIME: %f - PARENT PID: %d - CHILD ID: %d\n",run_time,getppid(),getpid());
    }
    }


    return 0;
}


