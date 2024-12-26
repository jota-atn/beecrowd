#include <stdio.h>

int main() {

	int codigoPecaUm, codigoPecaDois, numeroPecasUm, numeroPecasDois;
	double valorUnitarioUm, valorUnitarioDois;

	scanf("%d", &codigoPecaUm);
	scanf("%d", &numeroPecasUm);
	scanf("%lf", &valorUnitarioUm);
	scanf("%d", &codigoPecaDois);
	scanf("%d", &numeroPecasDois);
	scanf("%lf", &valorUnitarioDois);

	double valorTotal = valorUnitarioUm * numeroPecasUm + valorUnitarioDois * numeroPecasDois;

	printf("VALOR A PAGAR: R$ %.2lf\n", valorTotal);

	return 0;

}
