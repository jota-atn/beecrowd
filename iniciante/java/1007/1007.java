//QUESTÃO 1007 - Diferença

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
			            
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
							            
		int diferenca = (a * b - c * d);
								            
		System.out.println("DIFERENCA = " + diferenca);
	}
}
