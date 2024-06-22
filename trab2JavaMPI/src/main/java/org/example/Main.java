package org.example;

import mpi.*;
public class Main {
    public static void main(String[] args) {
        try{
            MPI.Init(args);
            int me = MPI.COMM_WORLD.Rank();
            int size = MPI.COMM_WORLD.Size();
            System.out.println("Processo " + me + " de tamanho " + size);
            MPI.Finalize();
        } catch (MPIException e){
            e.printStackTrace();
        }
    }
}