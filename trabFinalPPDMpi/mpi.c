#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>

// Estrutura para representar a memória compartilhada
typedef struct {
    void *memoria;
    int tamanho;
} SharedMemory;

// Inicialização do MPI
void inicializaMPI() {
    MPI_Init(NULL, NULL);
}

// Finalização do MPI
void finalizaMPI() {
    MPI_Finalize();
}

// Função de alocação de memória compartilhada
SharedMemory aloca(int tamanho) {
    SharedMemory shared_memory;

    // Calcula o tamanho necessário para cada processo
    int tamanho_por_processo = tamanho / world_size;

    // Aloca a memória localmente para cada processo
    void *memoria_local = malloc(tamanho_por_processo);

    // Coleta as memórias locais de todos os processos no processo 0
    MPI_Allgather(&memoria_local, tamanho_por_processo, MPI_BYTE, &shared_memory.memoria, tamanho_por_processo, MPI_BYTE, MPI_COMM_WORLD);

    // Define o tamanho total da memória
    shared_memory.tamanho = tamanho;

    return shared_memory;
}

// Função de escrita na memória compartilhada
void escreve(SharedMemory shared_memory, char *buf, int tamanho, int posicao) {
    // Copia os dados do buffer para a memória compartilhada na posição especificada
    memcpy(shared_memory.memoria + posicao, buf, tamanho);
}

// Função de leitura da memória compartilhada
void le(SharedMemory shared_memory, char *buf, int tamanho, int posicao) {
    // Copia os dados da memória compartilhada para o buffer na posição especificada
    memcpy(buf, shared_memory.memoria + posicao, tamanho);
}

int main() {
    // Inicialização do MPI
    inicializaMPI();

    // Obtém informações de rank e tamanho
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Tamanho total da memória compartilhada
    int tamanho_da_memoria = 1024;  // Ajuste conforme necessário

    // Aloca a memória compartilhada
    SharedMemory shared_memory = aloca(tamanho_da_memoria);

    // Operações de leitura e escrita
    if (world_rank == 0) {
        char mensagem[] = "Oi";
        escreve(shared_memory, mensagem, strlen(mensagem) + 1, 2);
    }

    MPI_Barrier(MPI_COMM_WORLD);  // Aguarda todos os processos terminarem de escrever

    if (world_rank == 1) {
        char buffer[5];
        le(shared_memory, buffer, 5, 3);
        printf("Processo %d leu: %s\n", world_rank, buffer);
    }

    // Finalização do MPI
    finalizaMPI();

    return 0;
}
