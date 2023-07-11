#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int counter_thread1 = 0;
int counter_thread2 = 0;
int counter_thread3 = 0;
char stop_condish = 'C';

void *thread_runner1 ();
void *thread_runner2 ();
void *thread_runner3 ();
void *thread_runner4 ();

int
main (int argc, char *argv[])
{

  pthread_t tid_1;
  pthread_attr_t attr_1;
  pthread_attr_init (&attr_1);
  pthread_create (&tid_1, &attr_1, thread_runner1, NULL);

  pthread_t tid_2;
  pthread_attr_t attr_2;
  pthread_attr_init (&attr_2);
  pthread_create (&tid_2, &attr_2, thread_runner2, NULL);

  pthread_t tid_3;
  pthread_attr_t attr_3;
  pthread_attr_init (&attr_3);
  pthread_create (&tid_3, &attr_3, thread_runner3, NULL);
  
  pthread_t tid_4;
  pthread_attr_t attr_4;
  pthread_attr_init (&attr_4);
  pthread_create (&tid_4, &attr_4, thread_runner4, NULL);

  
  pthread_join (tid_1, NULL);
  pthread_join (tid_2, NULL);
  pthread_join (tid_3, NULL);
  pthread_join (tid_4, NULL);
  
  printf("\nNumber of 1s =%d",counter_thread1);
  printf("\nNumber of 2s =%d",counter_thread2);
  printf("\nNumber of 3s =%d",counter_thread3);


}

void*
thread_runner1 ()
{
    while(stop_condish != 'q'){
        counter_thread1 ++;
        printf("1");
    }
  
  pthread_exit (0);
}

void*
thread_runner2 ()
{
  while(stop_condish != 'q'){
        counter_thread2 ++;
        printf("2");
  }
  pthread_exit (0);
}

void*
thread_runner3 ()
{
  while(stop_condish != 'q'){
        counter_thread3 ++;       
        printf("3");
  }
  pthread_exit (0);
}

void*
thread_runner4 ()
{
  while(stop_condish != 'q'){
       stop_condish = getchar();
  }
  pthread_exit (0);
}