#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <stdbool.h>

#define N_SENSORES 5 // Definindo o número de sensores
#define N_ATUADORES 3 // Definindo o número de atuadores
#define N_PROCESSAMENTO 2 // Definindo o número de unidades de processamento

int sensores[N_SENSORES]; // Array para armazenar os sensores
int atuadores[N_ATUADORES][2]; // Matriz para armazenar os atuadores e níveis de atividade

pthread_mutex_t mutex_atuadores = PTHREAD_MUTEX_INITIALIZER; // Mutex para controlar o acesso aos atuadores

// Função para gerar um sensor aleatório entre 0 e 1000
int gerarSensor() {
    return rand() % 1001;
}

// Função para inicializar os atuadores com atividade 0
void inicializarAtuadores() {
    for (int i = 0; i < N_ATUADORES; i++) {
        atuadores[i][0] = i; // Número do atuador
        atuadores[i][1] = 0; // Nível de atividade inicial
    }
}

// Função para imprimir os sensores e os atuadores
void imprimirSensoresAtuadores() {
    printf("Sensores:\n");
    for (int i = 0; i < N_SENSORES; i++) {
        printf("Sensor %d: %d\n", i + 1, sensores[i]);
    }

    printf("\nAtuadores:\n");
    for (int i = 0; i < N_ATUADORES; i++) {
        printf("Atuador %d - Nível de Atividade: %d\n", atuadores[i][0], atuadores[i][1]);
    }
    printf("\n");
}

// Função executada por cada unidade de processamento (thread)
void *threadUnidadeProcessamento(void *arg) {
    int unidade_id = *(int*)arg;
    while (1) {
        // Lógica da Central de Controle
        int sensor_id = rand() % N_SENSORES; // Selecionar um sensor aleatório
        int atuador_id = sensores[sensor_id] % N_ATUADORES; // Definir o atuador correspondente ao sensor
        int nivel_atividade = rand() % 101; // Gerar um nível de atividade aleatório entre 0 e 100

        pthread_mutex_lock(&mutex_atuadores); // Bloquear o acesso aos atuadores
        atuadores[atuador_id][1] = nivel_atividade; // Definir o nível de atividade do atuador

        // Imprimir a mensagem de alteração no painel do veículo
        printf("Alterando: Atuador %d com valor %d\n", atuadores[atuador_id][0], atuadores[atuador_id][1]);
        pthread_mutex_unlock(&mutex_atuadores); // Liberar o acesso aos atuadores

        sleep(rand() % 2 + 2); // Aguardar entre 2 e 3 segundos
    }
}

int main() {
    inicializarAtuadores();
    imprimirSensoresAtuadores();

    pthread_t threads[N_PROCESSAMENTO];

    // Criar threads para as unidades de processamento
    for (int i = 0; i < N_PROCESSAMENTO; i++) {
        pthread_create(&threads[i], NULL, threadUnidadeProcessamento, (void*)&i);
    }

    // Aguardar as threads de processamento terminarem (o que não ocorrerá neste exemplo)
    for (int i = 0; i < N_PROCESSAMENTO; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
