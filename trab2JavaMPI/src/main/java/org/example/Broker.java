package org.example;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import mpi.MPI;
import mpi.Status;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

@Data
@Getter
@Setter
public class Broker {
    private String address;
    private ArrayList<HashMap<String, String>> receivedContent = new ArrayList<>();
    private ArrayList<HashMap<Integer,Integer>> subscribers = new ArrayList<>();

    public static Broker getBroker() throws FileNotFoundException {
        Gson gson = new GsonBuilder().create();

        try (FileReader reader = new FileReader(System.getProperty("user.dir") + "/src/main/resources/broker.json")) {
            return gson.fromJson(reader, Broker.class);
        } catch (IOException e) {
            System.out.println("Erro lendo a file do broekr");
            throw new RuntimeException(e);
        }
    }

    public void teste() {
        System.out.println("Funcionou");
    }

    public void processReceive(String[] receivedMessage) {
        String str = Arrays.toString(receivedMessage);
        str = str.substring(2, str.length() - 2);
        String[] parts = str.split("=");
        System.out.println(parts[0]);
        System.out.println(parts[1]);
        HashMap<String, String> map = new HashMap<>();
        map.put(parts[0], parts[1]);
        receivedContent.add(map);
        System.out.println(receivedContent);
    }

    public void proccessRequest(String[] receivedMessage, int rankSource) {
        System.out.println("received a request from subscriber");

        //iterateFromPreviousRead(rankSource);
        String[] str = new String[]{"respondendo subscriber"};

        MPI.COMM_WORLD.Send(str, 0, str.length, MPI.OBJECT, rankSource, 0);
        System.out.println("received a request from subscriber");
    }



    public void iterateFromPreviousRead(int rankSource) {
        HashMap<Integer, Integer> previousRead = getSubscriberByRank(rankSource);
        if (previousRead != null) {
            int startIndex = previousRead.get(rankSource) + 1;
            for (int i = startIndex; i < receivedContent.size(); i++) {
                HashMap<String, String> content = receivedContent.get(i);
                // Processar o conteúdo aqui
            }
        } else {
            updateLatestRead(rankSource, -1);
        }
    }
    public HashMap<Integer, Integer> getSubscriberByRank(int rankSource) {
        for (HashMap<Integer, Integer> subscriber : subscribers) {
            if (subscriber.containsKey(rankSource)) {
                return subscriber;
            }
        }
        return null; // retorna null se nenhum HashMap com a chave rankSource for encontrado
    }
    //TODO vai ficar adicionando na lista, era para atualizar
    public void updateLatestRead(int rankSource, int latestReadIndex) {
        HashMap<Integer, Integer> latestRead = new HashMap<>();
        latestRead.put(rankSource, latestReadIndex);
        subscribers.add(latestRead);
    }
}
