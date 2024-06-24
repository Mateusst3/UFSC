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
    private HashMap<String, String> receivedContent = new HashMap<>();
    private HashMap<Integer,Integer> subscribers = new HashMap<>();

    public static Broker getBroker() throws FileNotFoundException {
        Gson gson = new GsonBuilder().create();

        try (FileReader reader = new FileReader(System.getProperty("user.dir") + "/src/main/resources/broker.json")) {
            return gson.fromJson(reader, Broker.class);
        } catch (IOException e) {
            System.out.println("Erro lendo a file do broekr");
            throw new RuntimeException(e);
        }
    }




    public void processReceive(String[] receivedMessage) {
        String str = Arrays.toString(receivedMessage);
        str = str.substring(2, str.length() - 2);
        String[] parts = str.split("=");
        receivedContent.put(parts[0], parts[1]);

        System.out.println("Conteudo recebido armazeanado: " + receivedContent);
    }

    public void proccessRequest(String[] receivedMessage, int rankSource) {

        HashMap<String, String> myMap = new HashMap<>();
        myMap.put("key1", "value1");
        myMap.put("key2", "value2");
        String string = Arrays.toString(receivedMessage);
        var finalStr = string.substring(1, (string.length()-1));
        ArrayList<String> response = iterateFromPreviousRead(rankSource, finalStr);
        String[] str = new String[]{response.toString()};


        MPI.COMM_WORLD.Send(str, 0, str.length, MPI.OBJECT, rankSource, 0);
        System.out.println("Broker enviou mensagem para " + rankSource + " : " + Arrays.toString(str));

    }



    public ArrayList<String> iterateFromPreviousRead(int rankSource, String receivedMessage) {
        int sizeBeforeRead = receivedContent.size();
        ArrayList<String> response = new ArrayList<>();
        Integer latestIndex = subscribers.get(rankSource);
        if (latestIndex != null) {
            for (int i = latestIndex; i < receivedContent.size(); i++) {
                response.add(receivedContent.get(receivedMessage));
                System.out.println("TENTANDO DAR GET EM "+ receivedMessage);
            }
        } else {
            updateLatestRead(rankSource, -1);
            iterateFromPreviousRead(rankSource, receivedMessage);
        }
        updateLatestRead(rankSource, sizeBeforeRead);
        return response;
    }

    //TODO vai ficar adicionando na lista, era para atualizar
    public void updateLatestRead(int rankSource, int latestReadIndex) {
        subscribers.put(rankSource, latestReadIndex);
    }
}
