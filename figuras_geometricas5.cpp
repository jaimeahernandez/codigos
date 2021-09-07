#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    float A, b, B, h;
    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN TRAPECIO..." << endl << endl;
    std::cout << "Digite el valor de la BASE MAYOR: " << endl;
    std::cin >> B;
    std::cout << "Digite el valor de la BASE MENOR: " << endl;
    std::cin >> b;
    std::cout << "Digite el valor de la ALTURA: " << endl;
    std::cin >> h;
    std::cout << endl;
    A=((B+b)/2)*h;
    system("cls");
    std::cout << "El area del TRAPECIO ES: " << A << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
    //DISEÑADO POR: JAIME ALBERTO HERNANDEZ JIMENEZ
}