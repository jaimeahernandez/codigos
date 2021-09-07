package com.mintic.proyectoinicial;

public class Carro {
    private String marca;
    private String modelo;
    private String descripcion;

    public Carro(String marca, String modelo, String descripcion) {
        this.marca = marca;
        this.modelo = modelo;
        this.descripcion = descripcion;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
    public String toString(int i){
        String cad="Carro No" +i+
                "\n=============================="+
                "\nMarca: "+getMarca()+
                "\nModelo: "+getModelo()+
                "\nDescripcion: "+getDescripcion()+"\n";
        return cad;
    }
}
