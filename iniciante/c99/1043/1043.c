#include <stdio.h>

int main() {

	double a, b, c;

	scanf("%lf", &a);
	scanf("%lf", &b);
	scanf("%lf", &c);

	if (a < (b + c) && b < (a + c) && c < (a + b))
		printf("Perimetro = %.1lf\n", (a + b + c));

	else
		printf("Area = %.1lf\n", ((a + b) * c)/2);

	return 0;

}
