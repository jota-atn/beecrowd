#include <stdio.h>
#include <math.h>

int main() {

	double PI = 3.14159;
	
	double raio;

	scanf("%lf", &raio);

	double area = pow(raio, 2.0) * PI;

	printf("A=%.4f\n", area);

	return 0;

}
