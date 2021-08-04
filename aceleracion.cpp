#include <iostream>
using namespace std;
int main(){
    double a,b,c;
    std::cout << "Ingresa el valor de Velocidad Final"<<endl;
    std::cin >> a;
    std::cout << "Ingresa el valor de Velocidad Inicial"<<endl;
    std::cin >> b;
    std::cout << "Ingresa el valor de Tiempo"<<endl;
    std::cin >> c;
    std::cout <<"El valor de la Aceleracion es: "<< (a-b)/c <<endl;
    system("pause");
    return EXIT_SUCCESS;
}