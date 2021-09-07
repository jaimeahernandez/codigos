#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    float A, D, d;
        std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN ROMBO..." << endl << endl;
    std::cout << "Digite el valor de la DIAGONAL MAYOR: " << endl;
    std::cin >> D;
    std::cout << "Digite el valor de la DIAGONAL MENOR: " << endl;
    std::cin >> d;
    std::cout << endl;
    A=D*d/2;
    system("cls");
    std::cout << "El area del ROMBO ES: " << A << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
    //DISEÑADO POR: JAIME ALBERTO HERNANDEZ JIMENEZ
}