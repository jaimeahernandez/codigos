#include <iostream>
using namespace std;
int main(){
    int edad;
    std::cout << "Ingrese la edad de su hijo: "<<endl;
    std::cin >> edad;
    if (edad>0 && edad<=6){
        std::cout << "Su hijo pertenece al grupo de la primera infancia"<<endl;
    }else if (edad>6 && edad<=12){
        std::cout << "Su hijo pertenece al grupo de la segunda infancia"<<endl;
    }else if (edad>12 && edad<18){
        std::cout << "Su hijo pertenece pertenece al grupo de los adolescentes"<<endl;
    }
    system("pause");
    return 0;
}