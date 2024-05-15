package org.ppd;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.locks.ReentrantLock;

class TarefaDeProcessamento implements Runnable {
    private final int dadoSensorial;
    private final Map<Integer, Integer> atuadores;
    private final ReentrantLock[] locks;
    private final Random random = new Random();
    private final int atuadorId;
    public TarefaDeProcessamento(int dadoSensorial, Map<Integer, Integer> atuadores, ReentrantLock[] locks) {
        this.dadoSensorial = dadoSensorial;
        this.atuadores = atuadores;
        atuadorId = dadoSensorial % atuadores.size();
        this.locks = locks;
    }

    private void alterarAtividade(int atuadorId, int atividade) throws Exception {
        double chance = random.nextDouble();
        if (chance < 0.2) {
            throw new Exception("Falha na alteração de atividade");
        }
        atuadores.put(atuadorId, atividade);
    }

    private void imprimir(int atuadorId, int atividade) throws Exception {
        double chance = random.nextDouble();
        if (chance < 0.2) {
            throw new Exception("Falha na impressão");
        }
        Impressora.impressaoUnica(String.format("%s definiu atividade do atuador %d para %d \n", Thread.currentThread().getName(), atuadorId, atividade));
    }
    //teste git config
    @Override
    public void run() {

        try {
            locks[atuadorId].lockInterruptibly(); // Bloquear o mutex do atuador de forma interruptível

            int atividade = random.nextInt(101); // Gerar nível de atividade entre 0 e 100

            // Criar as tarefas
            Callable<Void> alterarAtividadeTask = () -> {
                alterarAtividade(atuadorId, atividade);
                return null;
            };
            Callable<Void> imprimirTask = () -> {
                imprimir(atuadorId, atividade);
                return null;
            };

            // Executar as tarefas em paralelo e esperar até que ambas sejam concluídas
            List<Future<Void>> futures = ForkJoinPool.commonPool().invokeAll(Arrays.asList(alterarAtividadeTask, imprimirTask));

            for (Future<Void> future : futures) {
                future.get(); // Isso irá lançar uma exceção se a tarefa falhou
            }

            int delay = random.nextInt(1001) + 2000; // Gerar um valor aleatório entre 2000 e 3000
            Thread.sleep(delay); // Dormir por um período de tempo
        } catch (ExecutionException | InterruptedException ex) {
            Impressora.impressaoUnica(String.format("Falha: %s%n", atuadorId));
        } finally {
            locks[atuadorId].unlock(); // Garantir que o bloqueio seja liberado
        }

    }}