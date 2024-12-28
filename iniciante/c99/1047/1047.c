#include <stdio.h>

int main() {

	int hora_inicial, minuto_inicial, hora_final, minuto_final, qtd_horas = 0, qtd_minutos = 0;

	scanf("%d", &hora_inicial);
	scanf("%d", &minuto_inicial);
	scanf("%d", &hora_final);
	scanf("%d", &minuto_final);

	if (hora_inicial == hora_final && minuto_inicial == minuto_final)
		qtd_horas = 24;

	else {

		int minuto_aux = minuto_inicial;
		int contador = 0;

		while (1) {

			if (hora_inicial == hora_final && minuto_inicial == minuto_final) {
				qtd_minutos = (((minuto_inicial - minuto_aux) % 60) + 60) % 60 ;
				break;
			}

			minuto_inicial++;
			contador++;

			if (contador == 60) {
				qtd_horas++;
				contador = 0;
			}

			if (minuto_inicial == 60) {
				hora_inicial = (hora_inicial + 1) % 24;
				minuto_inicial = 0;
			}
		}
	}

	printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", qtd_horas, qtd_minutos);
		
	return 0;

}
