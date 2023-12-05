package org.example;

import mpi.MPI;
import org.example.api.ApiFunctions;

import java.lang.reflect.Array;
import java.util.List;
import java.util.Random;

public class Main {


    public static void main(String[] args) throws Exception {
        ApiFunctions apiFunctions = new ApiFunctions();
        MPI.Init(args);
        apiFunctions.aloca(200);
        try {
            apiFunctions.escreve(new String[]{"ola"}, 3, 180);
            String teste = "";
            apiFunctions.le(teste, 3, 180);

            apiFunctions.escreve(new String[]{"ola2"}, 4, 257);
            apiFunctions.le(teste, 4, 257);

            apiFunctions.escreve(new String[]{"ola4"}, 4, 312);
            apiFunctions.le(teste, 4, 312);

        } catch (Exception e) {
            e.printStackTrace();
        }

        MPI.Finalize();
    }


}