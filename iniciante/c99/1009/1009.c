#include <stdio.h>

int main() {
	
	char nomeVendedor[100];
	double salarioFixo, totalVendas;

	scanf("%99s", nomeVendedor);
	scanf("%lf", &salarioFixo);
	scanf("%lf", &totalVendas);

	double salario = salarioFixo + (0.15 * totalVendas);

	printf("TOTAL = R$ %.2lf\n", salario);

	return 0;

}
