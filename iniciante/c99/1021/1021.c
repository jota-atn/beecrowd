#include <stdio.h>
#include <stdlib.h>

int main() {

	double dinheiro;

	int notas[6] = {10000, 5000, 2000, 1000, 500, 200};
	int moedas[6] = {100, 50, 25, 10, 5, 1};

	scanf("%lf", &dinheiro);

	dinheiro = dinheiro * 100;

	//printf("%lf", dinheiro);

	printf("NOTAS:\n");
	for (int i = 0; i < 6; i++) {

		int saque = dinheiro / notas[i];
		int resto = dinheiro - saque * notas[i];
		dinheiro = resto;
		
		printf("%d nota(s) de R$ %d.00\n", saque, notas[i] / 100);
		
	}

	printf("MOEDAS:\n");
	for (int i = 0; i < 6; i++) {
		
		int saque_moedas = dinheiro / moedas[i];
		int resto_moedas = dinheiro - saque_moedas * moedas[i];
		dinheiro = resto_moedas;
			
		printf("%d moeda(s) de R$ %.2lf\n", saque_moedas, (double) moedas[i] / 100);

	}

	return 0;

}
