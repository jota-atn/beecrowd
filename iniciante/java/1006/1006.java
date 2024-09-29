//QUESTÃO 1006 - Média 2

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
	
		Scanner sc = new Scanner(System.in);
		        
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();
						            
		double media = ((a * 2) + (b * 3) + (c * 5)) / (2 + 3 + 5);
							            
		String saida = String.format("MEDIA = %.1f", media);
								        
		System.out.println(saida);
	}
}
