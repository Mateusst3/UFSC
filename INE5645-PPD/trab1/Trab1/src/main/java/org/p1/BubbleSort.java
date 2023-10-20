package org.p1;

class BubbleSort {

    // An optimized version of Bubble Sort
    static void bubbleSort(Integer[] arr, int n) {
        System.out.println("before");
        printArray(arr, n);
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were
            // swapped by inner loop, then break
            if (!swapped) break;
        }
        System.out.println("after");
        printArray(arr, n);
    }

    // Function to print an array
    static void printArray(Integer[] arr, int size) {
        int i;
        for (i = 0; i < size; i++) System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver program
    public static void main(String[] args) {
        Integer[] arr = { 64, 34, 25, 12, 22, 11, 90 };
        int n = arr.length;
        bubbleSort(arr, n);
        System.out.println("Sorted array: ");
        printArray(arr, n);
    }
}
