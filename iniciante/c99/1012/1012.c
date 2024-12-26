#include <stdio.h>
#include <math.h>

int main() {

	double a, b, c;
	const double PI = 3.14159;

	scanf("%lf", &a);
	scanf("%lf", &b);
	scanf("%lf", &c);

	double areaTriangulo = a * c / 2;
	double areaCirculo = PI * pow(c, 2);
	double areaTrapezio = (a + b) * c / 2;
	double areaQuadrado = pow(b, 2);
	double areaRetangulo = a * b;

	printf("TRIANGULO: %.3lf\n", areaTriangulo);
	printf("CIRCULO: %.3lf\n", areaCirculo);
	printf("TRAPEZIO: %.3lf\n", areaTrapezio);
	printf("QUADRADO: %.3lf\n", areaQuadrado);
	printf("RETANGULO: %.3lf\n", areaRetangulo);

	return 0;

}
