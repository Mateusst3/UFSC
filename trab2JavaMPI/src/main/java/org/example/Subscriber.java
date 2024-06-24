package org.example;


import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import mpi.MPI;
import mpi.Status;

import java.io.*;
import java.util.*;

public class Subscriber {
    private String address;
    private String brokerAddress;
    private ArrayList<String> tags;

    public static Subscriber getSubscriber() throws FileNotFoundException {
        Gson gson = new GsonBuilder().create();

        try (FileReader reader = new FileReader(System.getProperty("user.dir") + "/src/main/resources/subscriber.json")) {
            return gson.fromJson(reader, Subscriber.class);
        } catch (IOException e) {
            System.out.println("Erro lendo a file do pub");
            throw new RuntimeException(e);
        }
    }

    public void requestMessage(int rank){
        Random random = new Random();
        String randomTag = tags.get(random.nextInt(tags.size()));
        String[] str = new String[]{randomTag};

        MPI.COMM_WORLD.Send(str, 0, str.length, MPI.OBJECT, 0, 0);
        System.out.println("Subscriber " + rank + " enviou requisição para tag " + randomTag);

        String[] receivedMessage = new String[1];
        Status status = MPI.COMM_WORLD.Recv(receivedMessage, 0, 1, MPI.OBJECT, 0, MPI.ANY_TAG);
        System.out.println("Subscriber " + rank + " received message: " + Arrays.toString(receivedMessage));

    }

}
