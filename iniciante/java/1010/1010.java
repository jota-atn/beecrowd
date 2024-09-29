//QUESTÃO 1010 - Cálculo Simples

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
			            
		int codigoPecaUm = sc.nextInt();
		int numeroPecaUm = sc.nextInt();
		double valorUnitarioPecaUm = sc.nextDouble();
						            
		int codigoPecaDois = sc.nextInt();
		int numeroPecaDois = sc.nextInt();
		double valorUnitarioPecaDois = sc.nextDouble();
									            
		double valor = (numeroPecaUm * valorUnitarioPecaUm) + (numeroPecaDois * valorUnitarioPecaDois);
										            
		String saida = String.format("VALOR A PAGAR: R$ %.2f", valor);
											            
		System.out.println(saida);
	}
}

