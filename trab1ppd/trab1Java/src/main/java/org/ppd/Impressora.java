package org.ppd;

import java.util.concurrent.locks.ReentrantLock;

public class Impressora {
    private static final ReentrantLock lock = new ReentrantLock();

    public static void impressaoUnica(String mensagem) {
        lock.lock();
        try {
            System.out.println(mensagem);
            try {
                Thread.sleep(1000); // Deixe a mensagem visível por 1 segundo
            } catch (Exception e) {
                Thread.currentThread().interrupt();
            }
        } finally {
            lock.unlock();
        }
    }
}
