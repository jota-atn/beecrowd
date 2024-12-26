#include <stdio.h>

int main() {

	int valorSacado;
	int notas[7] = {100, 50, 20, 10, 5, 2, 1};

	scanf("%d", &valorSacado);

	printf("%d\n", valorSacado);

	for (int i = 0; i < 7; i++) {

		int resto = valorSacado % notas[i];
		int dinheiro = valorSacado / notas[i];		

		printf("%d nota(s) de R$ %d,00\n", dinheiro, notas[i]);	

		valorSacado = resto;
			
	}

	return 0;

}
