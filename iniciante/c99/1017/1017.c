#include <stdio.h>

int main() {

	int tempo, velocidadeMedia;
	
	scanf("%d", &tempo);
	scanf("%d", &velocidadeMedia);

	double consumo = velocidadeMedia / 12.0 * tempo;
	
	printf("%.3lf\n", consumo);
		
	return 0;

}
