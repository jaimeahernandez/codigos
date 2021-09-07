package com.mintic.proyectoinicial;

import java.util.ArrayList;

public class ArrayList1 {

    public static void main(String[] args) {
        ArrayList <Carro> carros=new ArrayList<Carro>();
        carros.add(new Carro("Ford","Fiesta","Compacto de 4 puertas ensamblado en Colombia"));
        carros.add(new Carro("BMW","Serie 2","Sedan Compacto coupe de 4 puertas ensamblado en Alemania"));
        carros.add(new Carro("Jaguar","XE","Sedan Compacto coupe de 2 puertas competidor del BMW Serie 3"));
        
        for(int i=0;i<carros.size();i++)
            System.out.println(carros.get(i).toString(i));
    }
    
}
