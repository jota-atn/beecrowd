#include <stdio.h>
#include <stdlib.h>

void swap(int *array, int i, int j) {
	int aux = array[j];
	array[j] = array[i];
	array[i] = aux;
}

void sort(int *array) {

	int len = sizeof(array) / sizeof(array[0]);

	for (int j = 0; j < len; j++) {
		for (int i = 0; i < len; i++) {
			if (array[i] > array[i+1])
				swap(array, i, i+1);
			}
	}
}

int main() {

	int a, b, c;

	int v[3];

	scanf("%d", &a);
	v[0] = a;
	scanf("%d", &b);
	v[1] = b;
	scanf("%d", &c);
	v[2] = c;
	
	sort(v);

	for (int i = 0; i < 3; i++) {
		printf("%d\n", v[i]);
	}

	printf("\n");

	printf("%d\n", a);
	printf("%d\n", b);
	printf("%d\n", c);

	return 0;

}

