import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int horarioInicial = sc.nextInt();
		int minutoInicial = sc.nextInt();
		int horarioFinal = sc.nextInt();
		int minutoFinal = sc.nextInt();

		int qtdHoras = 0, qtdMinutos = 0;

		if (horarioFinal == horarioInicial && minutoInicial == minutoFinal) {
			qtdHoras = 24;
		}

		else {
			
			int minutoAuxiliar = minutoInicial;
			int contador = 0;

			while (true) {

				if (horarioInicial == horarioFinal && minutoInicial == minutoFinal) {
					qtdMinutos = (((minutoInicial - minutoAuxiliar) % 60) + 60) % 60;
					break;
				}

				minutoInicial++;
				contador++;

				if (minutoInicial == 60) {
					horarioInicial = (horarioInicial + 1) % 24;
					minutoInicial = 0;
				}

				if (contador == 60) {
					qtdHoras++;
					contador = 0;
				} 
			}
		}

		System.out.println("O JOGO DUROU " + qtdHoras + " HORA(S) E " + qtdMinutos + " MINUTO(S)");

	}
}
