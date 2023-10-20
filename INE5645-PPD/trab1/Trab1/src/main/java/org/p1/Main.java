package org.p1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        List<Integer> arr = new ArrayList<Integer>();
        Random random = new Random();
        for(int i = 0; i < 1000; i++){
            arr.add(random.nextInt(0, 1000));

        }
        Integer[] arrF = arr.toArray(new Integer[0]);
        int lenght = arrF.length;
        BubbleSort.bubbleSort(arrF, lenght);
        QuickSort quickSort = new QuickSort();

        int min = 1000;
        int max = 0;
        for (Integer i : arrF){
            if(i < min){
                min = i;
            }
            if (i > max) {
                max = i;
            }
        }

        quickSort.sort(arrF, min, max);
    }
}