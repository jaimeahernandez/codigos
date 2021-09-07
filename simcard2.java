/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mintic.proyectoinicial;

/**
 *
 * @author usuario
 */
public class simcard2 {
    private String empresaTelefonia;
    private double saldo;
    private String numeroTelefono;
    private boolean celularApagado=true;
    private boolean modoAvionActivado=false;
    private boolean datosActivados=false;
    private int saldoDatos;

    public simcard2(String numeroTelefono) {
        this.numeroTelefono = numeroTelefono;
        this.empresaTelefonia= "HI";
        this.modoAvionActivado= false;
        this.datosActivados=false;
        this.celularApagado=true;
    }
    
    public void comprarDatos (int c){
        int costo = 0;
        
        if (c > saldo) {
            saldo -= 0;
            saldoDatos -= 0;
        }
        else if (c <= 10) {
            costo = c * 3000;
        }
        else if (c <= 30) {
            costo = ((c - 10) * 2500) + (c - (c - 10)) * 3000;
        }
        else {
            costo = ((c - 20) * 1500) + (c - (c - 20)) * 3000;
        }
        this.saldo -= costo;
        this.saldoDatos += c;
    }
    
    public void consumirDatos (int c){
        if (this.datosActivados)
            this.saldoDatos -= c;
    }
    
    public void llamar(int s){
        int valorSegundo=1;
        int costoCorriente, costoTotal;
        if(!this.celularApagado){
            if (s>0 && s<61){
                this.saldo-=s;
            }
        }
        else{
            costoCorriente=s-60;
            costoTotal=60*valorSegundo+costoCorriente*valorSegundo/2;
            this.saldo -= costoTotal;
        }
    }
    
    public void recargarSaldo(double s){
        this.saldo += s;
    }
    
    public void gestionarEncendidoCelular(){
        if(this.celularApagado)
            this.celularApagado=false;
        else{
            this.celularApagado=true;
            this.datosActivados=false;
            this.modoAvionActivado=false;
        }
    }
    
    public void gestionarModoAvion(){
        if(!this.modoAvionActivado && !this.celularApagado){
            this.datosActivados=false;
            this.modoAvionActivado=true;
        }
        else{
            this.modoAvionActivado=false;
        }
    }
    
    public void gestionarDatos(){
        this.datosActivados=! this.datosActivados;
    }

    public String getEmpresaTelefonia() {
        return empresaTelefonia;
    }

    public void setEmpresaTelefonia(String empresaTelefonia) {
        this.empresaTelefonia = empresaTelefonia;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getNumeroTelefono() {
        return numeroTelefono;
    }

    public void setNumeroTelefono(String numeroTelefono) {
        this.numeroTelefono = numeroTelefono;
    }

    public boolean isCelularApagado() {
        return celularApagado;
    }

    public void setCelularApagado(boolean celularApagado) {
        this.celularApagado = celularApagado;
    }

    public boolean isModoAvionActivado() {
        return modoAvionActivado;
    }

    public void setModoAvionActivado(boolean modoAvionActivado) {
        this.modoAvionActivado = modoAvionActivado;
    }

    public boolean isDatosActivados() {
        return datosActivados;
    }

    public void setDatosActivados(boolean datosActivados) {
        this.datosActivados = datosActivados;
    }

    public int getSaldoDatos() {
        return saldoDatos;
    }

    public void setSaldoDatos(int saldoDatos) {
        this.saldoDatos = saldoDatos;
    }
    
}

