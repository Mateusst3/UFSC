package org.example;

import mpi.*;
import runtime.daemonmanager.MPJBoot;

import javax.swing.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Map<Integer, String> interestsMp = new HashMap<>();
        LinkedList<EntitySend> messagesList = new LinkedList<EntitySend>();
        try {
            MPI.Init(args);
            int me = MPI.COMM_WORLD.Rank();
            int size = MPI.COMM_WORLD.Size();
            boolean running = true;
            while (running){
                MPI.COMM_WORLD.Barrier();
                if (me == 0) {
                    String addInterest = JOptionPane.showInputDialog(JOptionPane.getRootFrame(), "Você gostaria de adicionar um assunto? (true/false)");//Note: input can be null.
                    System.out.println("Você gostaria de adicionar um assunto? (true/false)");
                    System.out.println(addInterest);
                    if (addInterest.equals("true")) {
                        String interest = JOptionPane.showInputDialog(JOptionPane.getRootFrame(), "Escolha o assunto:");
                        String process = JOptionPane.showInputDialog(JOptionPane.getRootFrame(), "Escolha o processo:");
                        interestsMp.put(Integer.parseInt(process), interest);
                    }
                    else if (!interestsMp.isEmpty()) {
                        System.out.println("Escolha um assunto para mandar:");
                        interestsMp.forEach((key, value) -> System.out.println(key + ": " + value));
                        String interest = JOptionPane.showInputDialog(JOptionPane.getRootFrame(), "Escolha o Interesse:");
                        String message = JOptionPane.showInputDialog(JOptionPane.getRootFrame(), "Escreva a mensagem:");
                        messagesList.add(new EntitySend(interest, message));
                    }
                    if(!messagesList.isEmpty()){
                        EntitySend firstEntity = messagesList.getFirst();
                        interestsMp.forEach((key, value) -> {
                            if(value.equals(firstEntity.getInterest())){
                                System.out.println(firstEntity.getMessage());
                                String[] str = new String[]{firstEntity.getMessage()};
                                System.out.println("Enviando mensagem " + str.toString() + " para processo " + key);
                                MPI.COMM_WORLD.Isend(str,0, str.length, MPI.OBJECT, key, 0);
                            }
                        });
                    }
                }

                if (me != 0) {
                    String[] getRecieveMessage = new String[]{};
                    MPI.COMM_WORLD.Irecv(getRecieveMessage, 0, 100, MPI.CHAR, 0, 0);
                    if(getRecieveMessage.length > 0){
                        System.out.println("Processo " + me + " recebeu mensagem");
                    }
                }
                MPI.COMM_WORLD.Barrier();
            }

            MPI.Finalize();
        } catch (MPIException e) {
            e.printStackTrace();
        }
    }
}
