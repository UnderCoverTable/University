#include  <stdio.h>
#include  <unistd.h>
#include  <stdlib.h>
#include  <wait.h>
#include  <signal.h>


int cement_count = 0; // keeps track of cement made
int mix_cement = 1; // 0 when cement mixer should wait. 1 when it should start mixing

// signal received from brick layer to start mixing cement
void signal_brick(int sig){
	if (sig == SIGUSR2){
		printf("\nBricks laid. Cement Mixing has begun\n");
		mix_cement = 1;
	}
}


int main(){
	signal(SIGUSR2,signal_brick);
	
	pid_t cement_id;
	pid_t brick_id;
	
	cement_id = getpid();

	printf("\nPID of CementMixer= %d\n",cement_id); // PID of the cement mixer
	printf("Enter PID of BrickLayer:");
	scanf("%d",&brick_id); // PID of the brick layer
	
	fflush(stdout);
	
	while(2){
		while(mix_cement==0){ // stays in this loop until it recieves signal from bricklayer
		printf("Waiting for bricks to be laid now....\n");
		sleep(4); // delay so that it doesnt constantly print 
		}
		
		printf("\n~Cement is being made~\n");
		while (cement_count != 10){
			if (cement_count == 4 || cement_count == 9 ){
				printf("Made %d kg of cement..\n", cement_count+1); // prints progress after every 5 kg of cement is made
			}
			sleep(1);
			cement_count++;
		}
		if (cement_count == 10){
			printf("\nDelivered %d kg of cement!\n",cement_count);
			cement_count = 0;
			mix_cement = 0;
			kill(brick_id,SIGUSR1); // sends signal to bricklayer that cement has been mixed
		}
	}



	return 0;
}
