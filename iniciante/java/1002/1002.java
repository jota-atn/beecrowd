// QUESTÃO 1002 - Área do Círculo

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
			          	           
		double PI = 3.14159;
				            
		double raio = sc.nextDouble();
		double area = PI * (raio * raio);


		String saida = String.format("A=%.4f", area);
							            
							       
		System.out.println(saida);
	}
}
