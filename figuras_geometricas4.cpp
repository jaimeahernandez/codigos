#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    float A, b, h;
    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN PARALELOGRAMO..." << endl << endl;
    std::cout << "Digite el valor de la BASE: " << endl;
    std::cin >> b;
    std::cout << "Digite el valor de la ALTURA: " << endl;
    std::cin >> h;
    std::cout << endl;
    A=b*h;
    system("cls");
    std::cout << "El area del PARALELOGRAMO ES: " << A << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
    //DISEÑADO POR: JAIME ALBERTO HERNANDEZ JIMENEZ
}