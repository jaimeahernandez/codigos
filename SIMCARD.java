package com.mintic.proyectoinicial;      

public class SIMCARD{
    
    private String empresaTelefonia;
    private double saldo;
    private String numeroTelefono="3015328969";
    private boolean celularApagado;
    private boolean modoAvionActivado;
    private boolean datosActivados;
    private int saldoDatos;
    int costoTotal;
  
    public SIMCARD (String numetoTelefono){
        this.numeroTelefono=numeroTelefono;
        this.empresaTelefonia= "HI";
        this.modoAvionActivado= false;
        this.datosActivados=false;
        this.celularApagado=true;
    }
    
    public void comprarDatos (int c){
        int costoCorriente;
        int costoTotal;
        
        if (c>0){
            if(c>=0 && c<11){
                costoTotal=c*3000;
                if(this.saldo>costoTotal){
                    this.saldo -= costoTotal;
                }
            }
            else if(c<31){
                costoCorriente=c-10;
                costoTotal=costoCorriente*2500+10*3000;
                if(this.saldo>costoTotal){
                    this.saldo -= costoTotal;
                }
            }
            else{
                costoCorriente=c-20;
                costoTotal=costoCorriente*1500+20*3000;
                if(this.saldo>costoTotal){
                    this.saldo -= costoTotal;
                }
            }
            this.saldoDatos += c;
        }
    }
    public void consumirDatos (int c){
        if(this.celularApagado){
           this.saldoDatos -= costoTotal;
        }
    }
    public void llamar (int s){
        int valorSegundo=1;
        int costoCorriente, costoTotal;
        if(!this.celularApagado){
            if (s>0 && s<61){
               this.saldo-=s;
            }
            else{
                costoCorriente=s-60;
                costoTotal=60*valorSegundo+costoCorriente*valorSegundo/2;
                this.saldo -= costoTotal;
            }
        }
    }
    public void recargarSaldo(double s){
        this.saldo += s;
    }
    
    public void gestionarEncendidoCelular(){
        this.celularApagado =! this.celularApagado;
        if(this.celularApagado){
            this.datosActivados=false;
            this.modoAvionActivado=false;
        }
    }
    public void gestionarModoAvion(){
        if(this.celularApagado){
            this.modoAvionActivado=false;
            this.datosActivados=false;
            }
        }

    public void gestionarDatos(){ 
        this.datosActivados=! this.datosActivados;
    }
    
    public String getEmpresaTelefonia(){
        return this.empresaTelefonia;
    }
    
    public void setEmpresaTelefonia(String empresaTelefonia){
        this.empresaTelefonia=empresaTelefonia;
    }
    
    public double getSaldo(){
        return this.saldo;
    }
    
    public void setSaldo(double saldo){
        this.saldo=saldo;
    }    
    
    public String getNumeroTelefono(){
        return this.numeroTelefono;
    }    
    
    public void setNumeroTelefono(String numeroTelefono){
        this.numeroTelefono=numeroTelefono;
    }
    
    public boolean isCelularApagado(){
        return this.celularApagado;
    }
    
    public void setCelularApagado(boolean celularApagado){
        this.celularApagado=celularApagado;
    }
    
    public boolean isModoAvionActivado(){
        return this.modoAvionActivado;
    }
    
    public void setModoAvionActivado(boolean modoAvionActivado){
        this.modoAvionActivado=modoAvionActivado;
    }
    
    public boolean isDatosActivados(){
        return this.datosActivados;
    }
    
    public void setDatosActivados(boolean datosActivados){
        this.datosActivados=datosActivados;
    }
    
    public int getSaldoDatos(){
        return this.saldoDatos;
    }
    
    public void setSaldoDatos(int saldoDatos){
        this.saldoDatos=saldoDatos;
    }
}