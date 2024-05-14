package org.ppd;

import java.util.*;
import java.util.concurrent.*;

class Sensor implements Runnable {
    private final Map<Integer, Integer> actuators;
    private final Random random = new Random();

    public Sensor(Map<Integer, Integer> actuators) {
        this.actuators = actuators;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int data = random.nextInt(1001); // Gerar dado sensorial entre 0 e 1000
                int actuator = data % actuators.size();
                int activityLevel = random.nextInt(101); // Nível de atividade entre 0 e 100

                // Atualizar nível de atividade do atuador
                actuators.put(actuator, activityLevel);

                Thread.sleep(random.nextInt(5001) + 1000); // Intervalo entre 1s e 5s
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class Processor implements Runnable{
    private Integer activityLevel;
    private final Map<Integer, Integer> actuators;

    Processor(Integer activityLevel, Map<Integer, Integer> actuators) {
        this.activityLevel = activityLevel;
        this.actuators = actuators;
    }

    @Override
    public void run() {
        while(true){
            //doAnything
        }
    }
}

class ControlCenter implements Runnable {
    private final Map<Integer, Integer> actuators;
    private final Random random = new Random();

    public ControlCenter(Map<Integer, Integer> actuators) {
        this.actuators = actuators;
    }

    @Override
    public void run() {
        while (true) {
            // Escolher um atuador aleatório
            int actuator = random.nextInt(actuators.size());
            int activityLevel = random.nextInt(101); // Nível de atividade entre 0 e 100
            ExecutorService executorService = Executors.newFixedThreadPool(5);
            
//                System.out.println("Alterando: " + actuator + " com valor " + activityLevel);
//
//                // Simular alteração de nível de atividade do atuador
//                Thread.sleep(random.nextInt(2001) + 2000); // Manter por 2s a 3s
//
//                // Simular envio de mudança ao painel
//                System.out.println("Mudança enviada ao painel para o atuador " + actuator + " com valor " + activityLevel);
//                Thread.sleep(1000); // Manter no painel por 1s
        }
    }
}

public class AutonomousCarSystem {
    public static void main(String[] args) {
        final int N_SENSORS = 5;
        final int N_ATUADORES = 3;

        Map<Integer, Integer> actuators = new ConcurrentHashMap<>();

        // Inicializar todos os atuadores com atividade 0
        for (int i = 0; i < N_ATUADORES; i++) {
            actuators.put(i, 0);
        }

        new Thread(new Sensor(actuators)).start();

        // Criar thread da central de controle
        new Thread(new ControlCenter(actuators)).start();
    }
}
