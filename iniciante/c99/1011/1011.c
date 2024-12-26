#include <stdio.h>
#include <math.h>

int main() {

	int raio;
	const double PI = 3.14159;

	scanf("%d", &raio);

	double volume = ((4.0/3) * PI) * (pow(raio, 3));

	printf("VOLUME = %.3lf\n", volume);

	return 0;

}
