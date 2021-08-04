#include <iostream>
using namespace std;
int main(){
    int numero,i;
    std::cout << "Ingrese un numero entero del 1 al 10 :"<<endl;
    std::cin >> numero;
    for(int i=1;i<=10;i++){
        int multiplicacion=i * numero;
        std::cout<<numero<<" x "<< i <<" = "<<multiplicacion<<endl;
    }
    system("pause");
    return 0;
}