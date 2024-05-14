package org.ppd;

import java.util.*;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.*;

class Sensor implements Runnable {
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
                lock.lock(); // Bloquear o mutex
                try {
                    dadoSensorial = queue.poll(); // Consumir dados da fila
                } finally {
                    lock.unlock(); // Desbloquear o mutex
                }
                if (dadoSensorial != null) {
                    executorService.execute(new TarefaDeProcessamento(dadoSensorial, atuadores, locks));
                }
                //Thread.sleep(1000); // Intervalo para tentar consumir novamente
            }
        } catch (Exception e) {
            Thread.currentThread().interrupt();
        }
    }
}

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

}

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

public static class AutonomousCarSystem {
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
}}