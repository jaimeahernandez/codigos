#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

int main(){
    float a, A, b, B, h, D, d, r, pi= 3.141592;
    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN RECTANGULO..." << endl << endl;
    std::cout << "Digite el largo: " << endl;
    std::cin >> a;
    std::cout << "Digite el ancho: " << endl;
    std::cin >> b;
    std::cout << endl;
    A=a*b;
    system("cls");
    std::cout << "El area del RECTANGULO ES: " << A << endl << endl;

    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN TRIANGULO..." << endl << endl;
    std::cout << "Digite el valor de la BASE: " << endl;
    std::cin >> b;
    std::cout << "Digite el valor de la ALTURA: " << endl;
    std::cin >> h;
    std::cout << endl;
    A=b*h/2;
    std::cout << "El area del TRIANGULO ES: " << A << endl << endl;

    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN ROMBO..." << endl << endl;
    std::cout << "Digite el valor de la DIAGONAL MAYOR: " << endl;
    std::cin >> D;
    std::cout << "Digite el valor de la DIAGONAL MENOR: " << endl;
    std::cin >> d;
    std::cout << endl;
    A=D*d/2;
    std::cout << "El area del ROMBO ES: " << A << endl << endl;

    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN PARALELOGRAMO..." << endl << endl;
    std::cout << "Digite el valor de la BASE: " << endl;
    std::cin >> b;
    std::cout << "Digite el valor de la ALTURA: " << endl;
    std::cin >> h;
    std::cout << endl;
    A=b*h;
    std::cout << "El area del PARALELOGRAMO ES: " << A << endl << endl;

    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN TRAPECIO..." << endl << endl;
    std::cout << "Digite el valor de la BASE MAYOR: " << endl;
    std::cin >> B;
    std::cout << "Digite el valor de la BASE MENOR: " << endl;
    std::cin >> b;
    std::cout << "Digite el valor de la ALTURA: " << endl;
    std::cin >> h;
    std::cout << endl;
    A=((B+b)/2)*h;
    std::cout << "El area del TRAPECIO ES: " << A << endl << endl;

    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN CIRCULO..." << endl << endl;
    std::cout << "Digite el valor del RADIO: " << endl;
    std::cin >> r;
    std::cout << endl;
    A=pi*pow(r, 2);
    std::cout << "El area del CIRCULO ES: " << A << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
}