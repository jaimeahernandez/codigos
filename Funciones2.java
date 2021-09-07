package com.mintic.proyectoinicial;
      
public class Funciones2 {

    public static void main(String[] args) {
        // TODO code application logic here
    }
    
    public double makeChange(double itemCost, double dollarsProvided){
        double change=dollarsProvided-itemCost;
        return change;
    }
    double returnedchange=makeChange(3.60,5.75);
}
