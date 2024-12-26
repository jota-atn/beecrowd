#include <stdio.h>

int main() {

	int distanciaTotal;
	double combustivelGasto;

	scanf("%d", &distanciaTotal);
	scanf("%lf", &combustivelGasto);

	double consumoMedio = distanciaTotal / combustivelGasto;

	printf("%.3lf km/l\n", consumoMedio);

	return 0;

}
