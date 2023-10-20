package org.p1;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class RadixSortParallel {


    public static void parallelSort(long[] arr) {
        long[] output = new long[arr.length];

        int MAX_PART = 1_000_000;
        int numProc = Runtime.getRuntime().availableProcessors();
        int partL = Math
                .min((int) Math.ceil(arr.length / (double) numProc), MAX_PART);
        int parts = (int) Math.ceil(arr.length / (double) partL);

        Future[] threads = new Future[parts];
        ExecutorService worker = Executors.newFixedThreadPool(numProc);

        for (int i = 0; i < 8; i++) {
            int[][] counts = new int[parts][256];
            int radix = i;

            for (int j = 0; j < parts; j++) {
                int part = j;
                threads[j] = worker.submit(() -> {
                    for (int k = part * partL; k < (part + 1) * partL && k < arr.length;
                         k++) {
                        int chunk = (int) ((arr[k] >> (radix * 8)) & 255);
                        counts[part][chunk]++;
                    }
                });
            }
            barrier(parts, threads);

            int base = 0;
            for (int k = 0; k <= 255; k++) {
                for (int j = 0; j < parts; j++) {
                    int t = counts[j][k];
                    counts[j][k] = base;
                    base += t;
                }
            }

            for (int j = 0; j < parts; j++) {
                int part = j;
                threads[j] = worker.submit(() -> {
                    for (int k = part * partL;
                         k < (part + 1) * partL && k < arr.length;
                         k++) {

                        int chunk = (int) ((arr[k] >> (radix * 8)) & 255);
                        output[counts[part][chunk]] = arr[k];
                        counts[part][chunk]++;
                    }
                });
            }
            barrier(parts, threads);

            for (int j = 0; j < parts; j++) {
                int part = j;
                threads[j] = worker.submit(() -> {
                    for (int k = part * partL;
                         k < (part + 1) * partL && k < arr.length;
                         k++) {

                        arr[k] = output[k];
                    }
                });
            }
            barrier(parts, threads);
        }
        worker.shutdownNow();
    }

    private static void barrier(int parts, Future[] threads) {
        for (int j = 0; j < parts; j++) {
            try {
                threads[j].get();
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }
    }
}
