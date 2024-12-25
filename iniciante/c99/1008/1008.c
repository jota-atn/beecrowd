#include <stdio.h>

int main() {

	int numFuncionario, numHoras;
	double valorHora, salario;

	scanf("%d", &numFuncionario);
	scanf("%d", &numHoras);
	scanf("%lf", &valorHora);

	salario = numHoras * valorHora;

	printf("NUMBER = %d\n", numFuncionario);
	printf("SALARY = U$ %.2lf\n", salario);

	return 0;

}
