package org.example;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import mpi.MPI;
import mpi.Status;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

@Data
@Getter
@Setter
public class Broker {
    private String address;
    private ArrayList<HashMap<String, String>> receivedContent = new ArrayList<>();
    private HashMap<Integer,SubscriberRecord> subscribers = new HashMap<>();

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
        HashMap<String, String> newContent = new HashMap<>();
        newContent.put(parts[0], parts[1]);
        receivedContent.add(newContent);

        System.out.println("Conteudo recebido armazeanado: " + receivedContent);
    }

    public void proccessRequest(String[] receivedMessage, int rankSource) throws InterruptedException {
        String string = Arrays.toString(receivedMessage);
        String finalStr = new String(string.substring(1, (string.length()-1)));

        if (!subscribers.containsKey(rankSource)) {

            createLatestRead(rankSource, finalStr, Integer.valueOf(0));
        } else if (!subscribers.get(rankSource).getLatestReadBySubject().containsKey(finalStr)) {
            createLatestRead(rankSource, finalStr, Integer.valueOf(0));
        }

        ArrayList<String> response = iterateFromPreviousRead(rankSource, finalStr);

        String[] str = new String[]{response.toString()};


        MPI.COMM_WORLD.Send(str, 0, str.length, MPI.OBJECT, rankSource, 0);
        System.out.println("Broker enviou mensagem para " + rankSource + "." + "Offset do subscriber: " + subscribers.get(rankSource).getLatestReadBySubject());

    }



    public ArrayList<String> iterateFromPreviousRead(int rankSource, String receivedMessage) {
        int sizeBeforeRead = receivedContent.size();
        ArrayList<String> response = new ArrayList<>();

        var subscriberRecord = subscribers.get(rankSource);
        int latestIndex = subscriberRecord.getLatestReadBySubject().get(receivedMessage);
        for (int i = latestIndex; i < receivedContent.size(); i++) {
            HashMap<String, String> currentMap = receivedContent.get(i);
            if (currentMap.containsKey(receivedMessage)) {
                response.add(currentMap.get(receivedMessage));
            }

        }

        updateLatestRead(rankSource, receivedMessage, sizeBeforeRead);

        return response;
    }

    public void updateLatestRead(Integer rankSource, String receivedMessage, Integer latestReadIndex) {

        subscribers.get(rankSource).getLatestReadBySubject().put(receivedMessage, latestReadIndex);

    }

    public void createLatestRead(Integer rankSource, String receivedMessage, Integer latestReadIndex) {

        if (subscribers.containsKey(rankSource)) {
            subscribers.get(rankSource).getLatestReadBySubject().put(receivedMessage, latestReadIndex);

        } else {
            SubscriberRecord newRecord = new SubscriberRecord();
            subscribers.put(rankSource, newRecord);
            subscribers.get(rankSource).getLatestReadBySubject().put(receivedMessage, latestReadIndex);
        }

    }


}
