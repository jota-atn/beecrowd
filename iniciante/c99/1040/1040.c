#include <stdio.h>

int main() {

	double n1, n2, n3, n4, media;

	scanf("%lf", &n1);
	scanf("%lf", &n2);
	scanf("%lf", &n3);
	scanf("%lf", &n4);

	media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10;

	printf("Media: %.1lf\n", media);

	if (media >= 7)
		printf("Aluno aprovado.\n");

	if (media >= 5 && media < 7) {
			printf("Aluno em exame.\n");
				
			double nota_exame;
			scanf("%lf", &nota_exame);
			
			printf("Nota do exame: %.1lf\n", nota_exame);

			double media_final = (media + nota_exame) / 2; 

			if (media_final >= 5) 
				printf("Aluno aprovado.\n");

			else
				media = 0;
						
			printf("Media final: %.1lf\n", media_final);

	} 

	if (media < 5) 
		printf("Aluno reprovado.\n");

	return 0;

}
