package org.example;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import mpi.*;
import runtime.daemonmanager.MPJBoot;

import javax.swing.*;
import java.io.FileNotFoundException;
import java.lang.reflect.Type;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Map<Integer, String> interestsMp = new HashMap<>();
        ArrayList<HashMap<String, String>> receivedContent = new ArrayList<>();
        var publisher = Publisher.getPublisher();
        var broker = Broker.getBroker();
        var subscriber = Subscriber.getSubscriber();
        Random random = new Random();
        try {
            // cada processo vai passar por aqui, cada um com um rank 0,1,2
            // rank 0 broker, rank 1 publisher, rank 2 subscriber
            MPI.Init(args);
            int rank = MPI.COMM_WORLD.Rank();
            int size = MPI.COMM_WORLD.Size();



            while (true) {

                if (rank == 0 ) {
                    try {
                        String[] receivedMessage = new String[1];
                        Status status = MPI.COMM_WORLD.Recv(receivedMessage, 0, 1, MPI.OBJECT, MPI.ANY_SOURCE, MPI.ANY_TAG);

                        if (status.source % 2 == 0 ) {
                            //se source par, eh produtor
                            broker.processReceive(receivedMessage);
                        } else if (status.source % 2 != 0) {
                            broker.proccessRequest(receivedMessage, status.source);
                        }
                        //broker armazena numa lista
                        //broker tem outra lista de hashmap com o rank do processo consumidor e o indice da ultima mensagem lida
                        //ao receber requisicao do consumidor, itera sobre a lista a partir da ultima mensagem lida
                        //confere se a tag do consumidor esta na lista de interesses e envia, uma a uma
                    } catch (Exception e) {
                        System.out.println("Erro no broker na main");
                        e.printStackTrace();
                    }

                }
                //Processos pares são produtores
                else if (rank % 2 == 0) {
                    publisher.send(rank);
                    Thread.sleep(1000 + random.nextInt(1001)); // seguindo descrição do trabalho: requsicao aleatoriamenta a cada 1 a 2 segundos
                }
                //Processos impares serão consumidores
                else if (rank % 2 != 0 && rank != 0) {
                    subscriber.requestMessage(rank);
                    Thread.sleep(1000 + random.nextInt(1001)); // seguindo descrição do trabalho: requsicao aleatoriamenta a cada 1 a 2 segundos
                }


            }
        } catch (MPIException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        } finally {
            MPI.Finalize(); //TODO mover para finally
        }
    }
}
