package org.ppd;

import java.util.Map;
import java.util.Queue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.locks.ReentrantLock;

class CentralDeControle implements Runnable {
    private final Queue<Integer> queue;
    private final ReentrantLock lock;
    private final Map<Integer, Integer> atuadores;
    private final ReentrantLock[] locks;
    private final ExecutorService executorService;

    public CentralDeControle(Queue<Integer> queue, ReentrantLock lock, Map<Integer, Integer> atuadores, ReentrantLock[] locks, ExecutorService executorService) {
        this.queue = queue;
        this.lock = lock;
        this.atuadores = atuadores;
        this.locks = locks;
        this.executorService = executorService;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Integer dadoSensorial = null;
                lock.lock(); // Bloquear o mutex da fila para o Sensor não acessar
                try {
                    dadoSensorial = queue.poll(); // Consumir dados da fila
                } finally {
                    lock.unlock(); // Desbloquear o mutex
                }
                if (dadoSensorial != null) {
                    executorService.execute(new TarefaDeProcessamento(dadoSensorial, atuadores, locks));
                }
            }
        } catch (Exception e) {
            Thread.currentThread().interrupt();
        }
    }
}
