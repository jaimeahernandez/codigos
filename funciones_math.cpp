#include <iostream>
#include <math.h>
using namespace std;

int main(){
    std::cout << "DEMOSTRACION DE FUNCIONES MATEMATICAS EN C++" << endl << endl;
    std::cout << "Funcion FMAX para hallar el mayor de dos numeros: fmax(18.9, 18)=";
    std::cout << fmax(18.9, 18) << endl << endl;
    std::cout << "Funcion FMIN para hallar el menor de dos numeros: fmin(18.9, 18)=";
    std::cout << fmin(18.9, 18) << endl << endl;
    std::cout << "Funcion CEIL para redondear a una cifra superior: ceil(18.7)=";
    std::cout << ceil(18.7) << endl << endl;
    std::cout << "Funcion FLOOR para redondear a una cifra inferior: floor(18.7)=";
    std::cout << floor(18.7463) << endl << endl;
    std::cout << "Funcion POW para elevar un numero a una potencia: pow(9,2)=";
    std::cout << pow(9,2) << endl << endl;
    std::cout << "Funcion SQRT para hallar la raiz cuadrada de un número: sqrt(81)=";
    std::cout << sqrt(81) << endl << endl;
    std::cout << "Funcion HYPOT para hallar la hipotenusa de un triangulo: hypot(81)=";
    std::cout << hypot(3,4) << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
}