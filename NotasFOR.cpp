#include <iostream>
using namespace std;
 
//FUNCION
float promedioNotas(float cal1,float cal2, float cal3)
	{float Promedio;
	Promedio = (cal1+cal2+cal3)/3;
	return (Promedio);
	}
 
//PROCESO
int main()
{float nota1, nota2, nota3, i, n, notafinal;
std::cout<<"Ingrese cantidad de alumnos: ";
std::cin>>n;

//CICLO PARA NOTAS
for (i=1;i<=n;i++)
	{std::cout<<"\nIngrese la primera Nota: ";
	std::cin>>nota1;
	std::cout<<"Ingrese la segunda Nota: ";
	std::cin>>nota2;
	std::cout<<"Ingrese la tercera Nota: ";
	std::cin>>nota3;
	notafinal = promedioNotas(nota1,nota2,nota3);
    std::cout <<"El promedio de notas es "<<notafinal<<endl;
	
    //CONDICION ESPECIAL
	if (notafinal > 3.0)
		{std::cout<<"Asignatura APROBADA.\n";
		}
	else
		cout<<"Asignatura NO APROBADA.\n";
	}
    system("pause");
    return EXIT_SUCCESS; //JAIME ALBERTO HERNANDEZ JIMENEZ
}