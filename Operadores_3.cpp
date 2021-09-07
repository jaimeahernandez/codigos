#include <iostream>

using namespace std;

int main(){
    float lado_1, lado_2, base_mayor, base_menor, perimetro;
    std::cout << "PROGRAMA PARA HALLAR EL PERIMETRO DE UN TRAPECIO..." << endl << endl;
    std::cout << "Digite el lado 1: " << endl;
    std::cin >> lado_1;
    std::cout << endl;

    std::cout << "Digite el lado 2: " << endl;
    std::cin >> lado_2;
    std::cout << endl;

    std::cout << "Digite la Base Mayor: " << endl;
    std::cin >> base_mayor;
    std::cout << endl;

    std::cout << "Digite la Base Menor: " << endl;
    std::cin >> base_menor;
    std::cout << endl;

    perimetro=lado_1+lado_2+base_mayor+base_menor;

    std::cout << "El perimetro del trapecio es: " << perimetro << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
}
