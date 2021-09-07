
package com.mintic.proyectoinicial;

public class OOP {
    
    public static void main(String[] args) {
        System.out.println("Hola POO");
    }
    
    public class TV{
        
        int tamanoPantalla;
        int resolucion;
        int capacidadMemoria;
        int puertoUSB;
        int puertoHDMI;
        int audioOptico;
        String OS;
        String marca;
        String modelo;
        String versionHW;
        
        private String versionSW;
        
        public String getVersionSW(){
            return versionSW;
        }

        public boolean setVersionSW(String firmware){
            try{
                actualizarSWxUSB(firmware);
            }catch(Exception e){
                return false;
            }
            return true;
        }
        
        String sintonizador;
        
        public void encenderTV(){
        
        }
        public void apagarTV(){
        
        }
        
        /** 
         * En Cambiar Canal TV se incluye haciaArriba y haciaAbajo
         * @param haciaArriba cuando es True y haciaAbajo cuando es False
         */
        public void cambiarCanalTV(boolean haciaArriba){
        
        }
 
        public void cambiarCanalTV(int canalDeseado){
        
        }
        public void abrirAplicacion(){
        
        }
        private void cambiarCanalTV(boolean esArriba,boolean esAbajo,int canal){
        
        }
        private void actualizarSWxUSB(String firmware){
        
        }
        private void actualizarSWxWIFI(String firmware){
        
        }
       
    }
    
}
