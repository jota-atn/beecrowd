//QUESTÃO 1004 - Produto Simples

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
            	Scanner sc = new Scanner(System.in);
			            
		int a = sc.nextInt();
	        int b = sc.nextInt();

		int produto = a * b;

		System.out.println("PROD = " + produto);
	}
}
