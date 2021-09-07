#include <iostream>

using namespace std;

int main(){
    int a, b;
    std::cout << "Digite dos numeros para realizar las operaciones basicas...";
    std::cout << endl << endl << "Digite el primer numero a= " <<endl;
    std::cin >> a;
    std::cout << endl << "Digite el primer numero b= " <<endl;
    std::cin >> b;

    std::cout << endl << "El RESULTADO con operadores de asignación es...";
    std::cout << endl << endl;
    std::cout << "En este momento 'a' vale " << a << " y el valor de 'b' es " << b;
    std::cout << endl;
    std::cout << a << " += " << b << " = ";
    a += b;
    std::cout << a << endl << endl;

    std::cout << "En este momento 'a' vale " << a << " y el valor de 'b' es " << b;
    std::cout << endl;
    std::cout << a << " -= " << b << " = ";
    a -= b;
    std::cout << a << endl << endl;

    std::cout << "En este momento 'a' vale " << a << " y el valor de 'b' es " << b;
    std::cout << endl;
    std::cout << a << " *= " << b << " = ";
    a *= b;
    std::cout << a << endl << endl;

    std::cout << "En este momento 'a' vale " << a << " y el valor de 'b' es " << b;
    std::cout << endl;
    std::cout << a << " /= " << b << " = ";
    a /= b;
    std::cout << a << endl << endl;

    std::cout << "En este momento 'a' vale " << a << " y el valor de 'b' es " << b;
    std::cout << endl;
    std::cout << a << " %= " << b << " = ";
    a %= b;
    std::cout << a << endl << endl;

    system("pause");
    return EXIT_SUCCESS;
}