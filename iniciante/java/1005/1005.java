//QUESTÃO 1005 - Média 1

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
	
		Scanner sc = new Scanner(System.in);
		            
	        double a = sc.nextDouble();
		double b = sc.nextDouble();
					           
		double media = ((a * 3.5) + (b * 7.5)) / (7.5 + 3.5);
						            
		String saida = String.format("MEDIA = %.5f", media);
							            
		System.out.println(saida);
	}
}
