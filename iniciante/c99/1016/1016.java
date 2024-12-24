//QUESTÃO 1016 - Distância

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
	        Scanner sc = new Scanner(System.in);

	        int distancia = sc.nextInt();
	        int tempo = distancia * 2;

	        String saida = String.format("%d minutos", tempo);
	        System.out.println(saida);

		sc.close();
	}
}
