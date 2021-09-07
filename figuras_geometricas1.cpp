#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    float a, A, b;
    std::cout << "PROGRAMA PARA CALCULAR EL AREA DE UN RECTANGULO..." << endl << endl;
    std::cout << "Digite el largo: " << endl;
    std::cin >> a;
    std::cout << "Digite el ancho: " << endl;
    std::cin >> b;
    std::cout << endl;
    A=a*b;
    system("cls");
    std::cout << "El area del RECTANGULO ES: " << A << endl << endl;
    
    system("pause");
    return EXIT_SUCCESS;
    //DISEÑADO POR: JAIME ALBERTO HERNANDEZ JIMENEZ
}