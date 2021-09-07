#include <iostream>

using namespace std;

int main(){
    int a, b, suma, resta, mult, div, mod, resultado;
    std::cout << "Digite dos numeros para realizar las operaciones basicas...";
    std::cout << endl << endl << "Digite el primer numero a= " <<endl;
    std::cin >> a;
    std::cout << endl << "Digite el primer numero b= " <<endl;
    std::cin >> b;

    suma=a+b;
    resta=a-b;
    mult=a*b;
    div=a/b;
    mod=a%b;

    std::cout << endl << "El resultado con operadores aritmeticos es..." <<endl;
    std::cout << endl << endl;

    std::cout << a << "+" << b << "=" << suma << endl;
    std::cout << a << "-" << b << "=" << resta << endl;
    std::cout << a << "*" << b << "=" << mult << endl;
    std::cout << a << "/" << b << "=" << div << endl;
    std::cout << a << "%" << b << "=" << mod << endl;

    system("pause");
    return EXIT_SUCCESS;
}
