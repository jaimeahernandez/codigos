//Este es el primer codigo de C++ para el curso
#include <iostream> //iostream es la biblioteca estándar en C++ para acceder a entrada y/o salida
using namespace std; //namespace, no es más que una forma de crear un bloque y que toda funcion esta asociada a el
int main(){
    int a,b; //Se declara dos variables con entero
    std::cout << "Ingresa el primer numero"<<endl; //cout<< controla el flujo de datos que sale (Imprime salida)
    std::cin >> a;
    std::cout << "Ingresa el segundo numero"<<endl; //endl es para finalizar linea
    std::cin >> b;
    std::cout <<"La suma de los numeros es: "<< a+b <<endl; //instruccion para suma de numeros enteros
    std::cout <<"La resta de los numeros es: "<< a-b <<endl; //instruccion para resta de numeros enteros
    std::cout <<"La multiplicacion de los numeros es: "<< a*b <<endl; //instruccion para multiplicacion de enteros
    std::cout <<"La division de los numeros es: "<< a/b <<endl; //instruccion para division de numeros enteros
    std::cout <<"El residuo es: "<< a%b <<endl; //instruccion para obtener el residuos de dos numeros enteros
    std::cin.get();
    system("pause"); //permite hacer que tu programa espere a que se pulse una tecla
    return EXIT_SUCCESS;
}