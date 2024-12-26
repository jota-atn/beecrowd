#include <stdio.h>

int main() {

	int tipoCha;
	int respostas[5];

	scanf("%d", &tipoCha);

	int respostasCertas = 0;
	for (int i = 0; i < 5; i++) {

		scanf("%d", &respostas[i]);

		if (respostas[i] == tipoCha) {
			respostasCertas++;
		}
	}

	printf("%d\n", respostasCertas);

	return 0;
		
}
