package org.ppd;

import java.util.Queue;
import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

class Sensor extends Thread {
    private final Random random = new Random();
    private final Queue<Integer> queue;
    private final ReentrantLock lock;

    public Sensor(Queue<Integer> queue, ReentrantLock lock) {
        this.queue = queue;
        this.lock = lock;
    }

    @Override
    public void run() {
        try {
            while (true) {
                int data = random.nextInt(1001); // Gerar dado sensorial entre 0 e 1000
                lock.lock(); // Bloquear o mutex
                try {
                    queue.offer(data); // Colocar dados na fila
                } finally {
                    lock.unlock(); // Desbloquear o mutex
                }
                //System.out.println("Sensor produziu: " + data);
                Thread.sleep(random.nextInt(5001) + 1000); // Intervalo entre 1s e 5s
                //TODO dessa forma todos iniciam emitindo um dado sensorial e dormem quase que juntos
                //TODO talvez seja interessante melhorar isso para considerar no inicio também
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}