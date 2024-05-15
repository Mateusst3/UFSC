package org.ppd;

import java.util.*;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.*;


public class AutonomousCarSystem {
    public static void main(String[] args) {
        final int N_SENSORS;
        final int N_ATUADORES;
        final int N_UNIDADES_DE_PROCESSAMENTO = 10; // Defina o número de unidades de processamento

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o número de sensores: ");
        N_SENSORS = scanner.nextInt();

        System.out.println("Digite o número de atuadores: ");
        N_ATUADORES = scanner.nextInt();

        Queue<Integer> queue = new LinkedList<>();
        ReentrantLock lock = new ReentrantLock();

        ExecutorService sensorExecutorService = Executors.newFixedThreadPool(N_SENSORS);

        for (int i = 0; i < N_SENSORS; i++) {
            sensorExecutorService.execute(new Sensor(queue, lock));
        }

        Map<Integer, Integer> atuadores = new HashMap<>();
        ReentrantLock[] locks = new ReentrantLock[N_ATUADORES];

        for (int i = 0; i < N_ATUADORES; i++) {
            atuadores.put(i, 0); // Inicializa cada atuador com nível de atividade 0
            locks[i] = new ReentrantLock(); // Inicializa o mutex para cada atuador
        }

        ExecutorService processamentoExecutorService = Executors.newFixedThreadPool(N_UNIDADES_DE_PROCESSAMENTO);

        CentralDeControle centralDeControle = new CentralDeControle(queue, lock, atuadores, locks, processamentoExecutorService);
        new Thread(centralDeControle).start();
    }
}