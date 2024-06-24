package org.example;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import mpi.MPI;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Random;

@Data
@Getter
@Setter
public class Publisher {
    private String address;
    private String brokerAddress;
    private ArrayList<HashMap<String,String>> content;

    public static Publisher getPublisher() throws FileNotFoundException {
        Gson gson = new GsonBuilder().create();

        try (FileReader reader = new FileReader(System.getProperty("user.dir") + "/src/main/resources/publisher.json")) {
            return gson.fromJson(reader, Publisher.class);
        } catch (IOException e) {
            System.out.println("Erro lendo a file do sub");
            throw new RuntimeException(e);
        }
    }


    public void teste() {
        System.out.println("Publisher");
    }

    public void send(int rank) {
        Random random = new Random();
        int randomIndex = random.nextInt(content.size());
        try {
            //Pega um conteudo aleatorio da lista de conteudos, passando o par assunto/mensagem
            String[] str = new String[]{content.get(randomIndex).toString()};

            System.out.printf("Publisher %d Enviando mensagem %s para processo adicionar aqui depois o assunto%n", rank, Arrays.toString(str));
            MPI.COMM_WORLD.Send(str, 0, str.length, MPI.OBJECT, 0, 0);
            Thread.sleep(1000 + random.nextInt(1001));

        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }}
