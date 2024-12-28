#include <stdio.h>

int main() {

	int duracao_total;

	scanf("%d", &duracao_total);

	printf("%d:%d:%d\n", (duracao_total / 3600), (duracao_total / 60 % 60), duracao_total % 60);
		
	return 0;

}
