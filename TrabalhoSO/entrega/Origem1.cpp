#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define MAX_NAVES 20

sem_t sem_naves;         // sem�foro para controlar acesso �s naves
int naves[MAX_NAVES][2]; // array com as coordenadas das naves

void* movimentaNaves(void* arg)
{
    int i;
    while (1)
    {
        sem_wait(&sem_naves);
        for (i = 0; i < MAX_NAVES; i++)
        {
            // move a nave para a esquerda
            naves[i][0]--;
            // verifica se a nave foi abatida
            if (naves[i][1] != -1 && /* nave n�o foi abatida */
                /* colis�o com um foguete */
                /* verifica todas as posi��es de foguetes */
                /* se houver colis�o, marca nave como abatida */
                )
            {
                naves[i][1] = -1; // marca nave como abatida
                // atualiza score do jogador
            }
        }
        sem_post(&sem_naves);
        usleep(100000); // espera 100ms
    }
}

int main()
{
    int i;

    // inicializa array de naves
    for (i = 0; i < MAX_NAVES; i++)
    {
        naves[i][0] = 80;              // posi��o inicial x
        naves[i][1] = rand() % 7 + 10; // posi��o inicial y (aleat�ria)
    }

    // cria sem�foro para controlar acesso �s naves
    sem_init(&sem_naves, 0, 1);

    // cria thread para controlar movimento das naves
    pthread_t threadNaves;
    pthread_create(&threadNaves, NULL, movimentaNaves, NULL);

    // espera pelo fim do jogo
    pthread_join(threadNaves, NULL);

    return 0;
}
