package org.example.api;

import mpi.Datatype;
import mpi.MPI;
import sun.misc.Unsafe;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ApiFunctions {
    private ApiModel localMemoryObj = new ApiModel();

    public void aloca(int tamanho) throws Exception {
        MPI.COMM_WORLD.Barrier();
        int tamanhoTotal = tamanho * MPI.COMM_WORLD.Size();
        if (tamanho != tamanhoTotal / MPI.COMM_WORLD.Size()) {
            throw new Exception("Sem processos necessarios para a memoria");
        }
        Character[] novoArray = new Character[localMemoryObj.localMemory.length + tamanho];
        System.arraycopy(localMemoryObj.localMemory, 0, novoArray, 0, localMemoryObj.localMemory.length);
        localMemoryObj.localMemory = novoArray;
        localMemoryObj.totalMemoryAllocated = tamanho;
        MPI.COMM_WORLD.Barrier();
    }

    public void escreve(String[] buf, int tamanho, long posicao) throws Exception {
        MPI.COMM_WORLD.Barrier();
        int rank2Send = (int) Math.ceil(posicao / localMemoryObj.totalMemoryAllocated);
        if (MPI.COMM_WORLD.Rank() != rank2Send) {
            MPI.COMM_WORLD.Isend(buf, 0, 1, MPI.OBJECT, rank2Send, 0);
        } else {
            String[] rec = new String[1];
            MPI.COMM_WORLD.Recv(rec, 0, 1, MPI.OBJECT, MPI.ANY_SOURCE, MPI.ANY_TAG);
            System.out.println("o processo " + MPI.COMM_WORLD.Rank() + " escreveu " + rec[0] + " na posicao " + posicao);
            int pos = (int) (posicao % localMemoryObj.totalMemoryAllocated);
            for (String s : rec) {
                for (Character c : s.toCharArray()) {
                    if (tamanho + posicao <= (long) localMemoryObj.totalMemoryAllocated * (MPI.COMM_WORLD.Rank() + 1)) {
                        localMemoryObj.localMemory[pos] = c;
                        pos++;
                    } else {
                        throw new Exception("não é possível escrever na memória nesse espaço");
                    }
                }
            }
        }
        MPI.COMM_WORLD.Barrier();
    }

    public void le(String buf, Integer tamanho, Integer posicao) throws Exception {
        MPI.COMM_WORLD.Barrier();
        int rank2Read = (int) Math.ceil(posicao / localMemoryObj.totalMemoryAllocated);
        if (MPI.COMM_WORLD.Rank() == rank2Read) {
            long maxValue = (long) localMemoryObj.totalMemoryAllocated * (MPI.COMM_WORLD.Rank());
            if (tamanho + posicao <= (long) localMemoryObj.totalMemoryAllocated * (MPI.COMM_WORLD.Rank() + 1)) {
                StringBuilder bufBuilder = new StringBuilder(buf);
                for (int i = (int) (posicao - maxValue); i < (posicao - maxValue) + tamanho; i++) {
                    bufBuilder.append(localMemoryObj.localMemory[i]);
                }
                buf = bufBuilder.toString();
                System.out.println("o processo " + MPI.COMM_WORLD.Rank() + " leu " + buf + " na posicao " + posicao);
            } else {
                throw new Exception("não é possível escrever na memória nesse espaço");
            }
        }
        MPI.COMM_WORLD.Barrier();
    }
}
