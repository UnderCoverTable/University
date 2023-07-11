#include  <stdio.h>
#include  <unistd.h>
#include  <stdlib.h>
#include  <wait.h>
#include  <signal.h>


int brick_count = 0; // keeps track of bricks laid
int cement_arrived = 0; // 0 if no cement. 1 if cement has arrived

// Signal that is recieved from cement mixer, that cement has arrived.
void signal_cement(int sig){
	if (sig == SIGUSR1){
		printf("\nReceived Cement. Starting to lay bricks\n");
		cement_arrived = 1;
	}
}

int main(){
	signal(SIGUSR1,signal_cement);
	
	
	pid_t cement_id;
	pid_t brick_id;
	
	brick_id = getpid();

	printf("\nPID of BrickLayer= %d\n",brick_id); // PID of the bricklayer
	printf("Enter PID of CementMixer:");
	scanf("%d",&cement_id); // PID of the cement mixer
	printf("\n");
	
	
	fflush(stdout);
	
	while(1){
		while (cement_arrived == 0){ // stays in this loop until recieveing signal from cement mixer
		printf("Waiting for cement to be delivered now....\n");
		sleep(3); // delay so that it doesnt constantly print 
		
		}
		printf("\n~Laying bricks~\n");
		while(brick_count != 15){
			if (brick_count == 4 || brick_count == 9 || brick_count == 14){
				printf("Laid %d Bricks..\n", brick_count+1); // prints progress of laid bricks, every 5 bricks
			}
			sleep(1);
			brick_count++;
		}
		if (brick_count == 15){ 
			printf("\nAll %d bricks laid!\n",brick_count);
			brick_count = 0;
			cement_arrived = 0;
			kill(cement_id,SIGUSR2); // sends signal to cement mixer that bricks have been laid
		}
	}
	


	return 0;
}
