#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
void *ThreadFunc(void *arg);
/* Create and initialise the mutex for use. */
pthread_mutex_t cntrMutex = PTHREAD_MUTEX_INITIALIZER;
/* The global resource our mutex is to protect. */
int cntr;
int main(int argc, char *argv[])
{
    pthread_t idThread1;
    pthread_t idThread2;
    puts("Let’s create some threads!");
    pthread_create(&idThread1, NULL, ThreadFunc, (void *)21);
    pthread_create(&idThread2, NULL, ThreadFunc, (void *)14);
    pthread_join(idThread1, NULL);
    pthread_join(idThread2, NULL);
}

void *ThreadFunc(void *arg)
{
    int i, nMax, n;
    /* Get the value of the argument passed in. */
    nMax = (int)arg;
    /* Do stuff! */
    for (i = 0; i < nMax; i++)
    {
        n = rand() % nMax;
        pthread_mutex_lock(&cntrMutex);
        for (cntr = 0; cntr < n; i++)
            printf("Loop %d: La la la!\n", cntr + 1);
        pthread_mutex_unlock(&cntrMutex);
    }
    return NULL;
}