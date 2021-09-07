package com.mintic.proyectoinicial;

import java.util.Scanner;

public class CalculoWBGT {
    
    //FORMULA DE CALCULO DEL WBGT EXTERIOR
    public static double WBGTExterior(double numero1,double numero2,double numero3){
        double indiceWBGT=(numero1*0.7)+(numero2*0.2)+(numero3*0.1);
        return indiceWBGT;
    }
    
    public static void main(String[] args) {
        //DECLARACION DE VARIABLES
        Scanner entrada=new Scanner(System.in);
        char letra1;
        char letra2;
        String valoracion;
                
        //INGRESO DE DATOS PARA EL CALCULO DEL WBGT EXTERIOR
        double n1;
        double n2;
        double n3;
        double n4;
        System.out.println("Indique el valor de la Temperatura Húmeda: ");
        n1=entrada.nextDouble();
        System.out.println("Indique el valor de la Temperatura de Globo: ");
        n2=entrada.nextDouble();
        System.out.println("Indique el valor de la Temperatura Seca: ");
        n3=entrada.nextDouble();
        System.out.println("Indique el valor de la Carga Termica: ");
        n4=entrada.nextDouble();
        
        //LLAMADA DE FUNCION WBGT EXTERIOR(FUNCTION CALL)
        double returnedindiceWBGT=WBGTExterior(n1,n2,n3);
        System.out.println("El Indice WBGT Exterior es:"+returnedindiceWBGT+" Grados Centigrados");
               
        //VALORACION DE LA CARGA TERMICA
        if (n4<200){
            System.out.println("La Carga Termica es LIVIANO");
        }else if (n4>=200 && n4<300){
            System.out.println("La Carga Termica es MODERADO");
        }else if (n4>=300 && n4<400){
            System.out.println("La Carga Termica es PESADO");
        }else{
            System.out.println("La Carga Termica es MUY PESADO");
        }           
        //SELECCION DE CICLO Y CARGA DE TRABAJO POR EL USUARIO
        System.out.println("Indique el Ciclo de Trabajo(C,A,B,D): ");
        letra1=entrada.next().charAt(0);
        System.out.println("Indique la Carga de Trabajo(L,M,P,H): ");
        letra2=entrada.next().charAt(0);

        //CRITERIOS DE VALORACION DEL RIESGO
              
        if (letra1=='C' && letra2=='L'){
            int LimiteAccion1=28;
            int LimitePermisible1=31;
            System.out.println("El limite de accion es: "+LimiteAccion1);
            System.out.println("y El Limite permisible es: "+LimitePermisible1);
            if (returnedindiceWBGT<LimiteAccion1){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion1+" Grados Centigrados");
            }else if (returnedindiceWBGT>LimiteAccion1 && returnedindiceWBGT<LimitePermisible1){
                valoracion=("El riesgo es MEDIO");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible1);     
            }
            System.out.println(valoracion);
        }else if (letra1=='A' && letra2=='L'){
            int LimiteAccion2=28;
            int LimitePermisible2=31;
            System.out.println("El limite de accion es: "+LimiteAccion2);
            System.out.println("y El Limite permisible es: "+LimitePermisible2);
            if (returnedindiceWBGT<LimiteAccion2){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion2);
            }else if (returnedindiceWBGT>LimiteAccion2 && returnedindiceWBGT<LimitePermisible2){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible2);
            }
            System.out.println(valoracion);
        }else if (letra1=='B' && letra2=='L'){
            float LimiteAccion3=29.5f;
            int LimitePermisible3=32;
            System.out.println("El limite de accion es: "+LimiteAccion3);
            System.out.println("y El Limite permisible es: "+LimitePermisible3);
            if (returnedindiceWBGT<LimiteAccion3){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion3);
            }else if (returnedindiceWBGT>LimiteAccion3 && returnedindiceWBGT<LimitePermisible3){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible3);
            }
            System.out.println(valoracion);
        }else if (letra1=='D' && letra2=='L'){
            int LimiteAccion4=30;
            float LimitePermisible4=32.5f;         
            System.out.println("El limite de accion es: "+LimiteAccion4);
            System.out.println("y El Limite permisible es: "+LimitePermisible4);
            if (returnedindiceWBGT<LimiteAccion4){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion4);
            }else if (returnedindiceWBGT>LimiteAccion4 && returnedindiceWBGT<LimitePermisible4){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible4);
            }
            System.out.println(valoracion);
        }else if (letra1=='C' && letra2=='M'){
            int LimiteAccion5=25;
            int LimitePermisible5=28;               
            System.out.println("El limite de accion es: "+LimiteAccion5);
            System.out.println("y El Limite permisible es: "+LimitePermisible5);
            if (returnedindiceWBGT<LimiteAccion5){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion5);
            }else if (returnedindiceWBGT>LimiteAccion5 && returnedindiceWBGT<LimitePermisible5){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible5);
            }
            System.out.println(valoracion);
        }else if (letra1=='A' && letra2=='M'){
            int LimiteAccion6=26;
            int LimitePermisible6=29;                 
            System.out.println("El limite de accion es: "+LimiteAccion6);
            System.out.println("y El Limite permisible es: "+LimitePermisible6);
            if (returnedindiceWBGT<LimiteAccion6){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion6);
            }else if (returnedindiceWBGT>LimiteAccion6 && returnedindiceWBGT<LimitePermisible6){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible6);
            }
            System.out.println(valoracion);
        }else if (letra1=='B' && letra2=='M'){
            int LimiteAccion7=27;
            int LimitePermisible7=30;                        
            System.out.println("El limite de accion es: "+LimiteAccion7);
            System.out.println("y El Limite permisible es: "+LimitePermisible7);
            if (returnedindiceWBGT<LimiteAccion7){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion7);
            }else if (returnedindiceWBGT>LimiteAccion7 && returnedindiceWBGT<LimitePermisible7){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible7);
            }
            System.out.println(valoracion);
        }else if (letra1=='D' && letra2=='M'){
            int LimiteAccion8=29;
            float LimitePermisible8=31.5f;                        
            System.out.println("El limite de accion es: "+LimiteAccion8);
            System.out.println("y El Limite permisible es: "+LimitePermisible8);
            if (returnedindiceWBGT<LimiteAccion8){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion8);
            }else if (returnedindiceWBGT>LimiteAccion8 && returnedindiceWBGT<LimitePermisible8){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible8);
            }
            System.out.println(valoracion);
        }else if (letra1=='A' && letra2=='P'){
            int LimiteAccion9=24;
            float LimitePermisible9=27.5f;                     
            System.out.println("El limite de accion es: "+LimiteAccion9);
            System.out.println("y El Limite permisible es: "+LimitePermisible9);
            if (returnedindiceWBGT<LimiteAccion9){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion9);
            }else if (returnedindiceWBGT>LimiteAccion9 && returnedindiceWBGT<LimitePermisible9){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible9);
            }
            System.out.println(valoracion);
        }else if (letra1=='B' && letra2=='P'){
            float LimiteAccion10=25.5f;
            int LimitePermisible10=29;                       
            System.out.println("El limite de accion es: "+LimiteAccion10);
            System.out.println("y El Limite permisible es: "+LimitePermisible10);
            if (returnedindiceWBGT<LimiteAccion10){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion10);
            }else if (returnedindiceWBGT>LimiteAccion10 && returnedindiceWBGT<LimitePermisible10){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible10);
            }
            System.out.println(valoracion);
        }else if (letra1=='D' && letra2=='P'){
            int LimiteAccion11=28;
            float LimitePermisible11=30.5f;                      
            System.out.println("El limite de accion es: "+LimiteAccion11);
            System.out.println("y El Limite permisible es: "+LimitePermisible11);
            if (returnedindiceWBGT<LimiteAccion11){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion11);
            }else if (returnedindiceWBGT>LimiteAccion11 && returnedindiceWBGT<LimitePermisible11){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible11);
            }
            System.out.println(valoracion);
        }else if (letra1=='B' && letra2=='H'){
            float LimiteAccion12=24.5f;
            int LimitePermisible12=28;         
            System.out.println("El limite de accion es: "+LimiteAccion12);
            System.out.println("y El Limite permisible es: "+LimitePermisible12);
            if (returnedindiceWBGT<LimiteAccion12){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion12);
            }else if (returnedindiceWBGT>LimiteAccion12 && returnedindiceWBGT<LimitePermisible12){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible12);
            }
            System.out.println(valoracion);
        }else if (letra1=='D' && letra2=='H'){
            int LimiteAccion13=27;
            int LimitePermisible13=30;            
            System.out.println("El limite de accion es: "+LimiteAccion13);
            System.out.println("y El Limite permisible es: "+LimitePermisible13);
            if (returnedindiceWBGT<LimiteAccion13){
                valoracion=("El riesgo es BAJO.El WBGT Exterior se encuentra por debajo de: "+LimiteAccion13);
            }else if (returnedindiceWBGT>LimiteAccion13 && returnedindiceWBGT<LimitePermisible13){
                valoracion=("El riesgo es MEDIO. El WBGT se encuentra entre el Limite de Accion y el permisible");
            }else{
                valoracion=("El riesgo es ALTO. El WBGT Exterior se encuentra por encima de: "+LimitePermisible13);
            }
            System.out.println(valoracion);
        }
    }
}