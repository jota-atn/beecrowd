#include <stdio.h>

int main() {

	int codigo, quantidade;
	double precos[5] = {4.00, 4.50, 5.00, 2.00, 1.50};

	scanf("%d", &codigo);
	scanf("%d", &quantidade);
	
	double preco = precos[codigo-1];
	double total = preco * quantidade;

	printf("Total: R$ %.2lf\n", total);

	return 0;

}
