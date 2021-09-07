#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

int main(){
    float A, r, pi= 3.141592;
    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN CIRCULO..." << endl << endl;
    std::cout << "Digite el valor del RADIO: " << endl;
    std::cin >> r;
    std::cout << endl;
    A=pi*pow(r, 2);
    system("cls");
    std::cout << "El area del CIRCULO ES: " << A << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
    //DISEÑADO POR: JAIME ALBERTO HERNANDEZ JIMENEZ
}