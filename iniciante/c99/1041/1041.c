#include <stdio.h>

int main() {

	double x, y;

	scanf("%lf", &x);
	scanf("%lf", &y);

	if (x > 0) {
		if (y > 0) 
			printf("Q1\n");

		else {
			if (y < 0) 
				printf("Q4\n");

			else 
				printf("Eixo X\n");
		}
	}

	else if (x < 0) {
		if (y < 0) 
			printf("Q3\n");
	
		else {
			if(y > 0)
				printf("Q2\n");
			
			else
				printf("Eixo X\n");

		}
	}

	else {
		if (x == 0 && y != 0)
			printf("Eixo Y\n");

		else
			printf("Origem\n");
	}
	
	return 0;

}
