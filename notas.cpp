#include <iostream>
using namespace std;
int main(){
    float a,b,c,d,promedio;
    std::cout << "Ingrese el valor de la primera nota: "<<endl;
    std::cin >> a;
    std::cout << "Ingrese el valor de la segunda nota: "<<endl;
    std::cin >> b;
    std::cout << "Ingrese el valor de la tercera nota: "<<endl;
    std::cin >> c;
    std::cout << "Ingrese el valor de la cuarta nota: "<<endl;
    std::cin >> d;
    promedio=(a+b+c+d)/4;
    if (promedio>=3.5 && promedio<=5){
        std::cout << "APROBADO: "<< promedio <<endl;
    }else if(promedio>=3 && promedio<3.5){
        std::cout << "No tiene aprobada la materia, pero tiene la oportunidad de recuperar: "<< promedio <<endl;
    }else if(promedio<3.0){
        std::cout << "NO APROBADO: "<< promedio <<endl;
    }
    system("pause");
    return EXIT_SUCCESS; //JAIME ALBERTO HERNANDEZ JIMENEZ
}