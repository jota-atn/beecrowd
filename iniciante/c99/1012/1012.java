//QUESTÃO 1012 - Área

import java.io.IOException;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) throws IOException {
   
	   	Scanner sc = new Scanner(System.in);
			            
	        double a = sc.nextDouble();
 	        double b = sc.nextDouble();
 	        double c = sc.nextDouble();
						            
		double PI = 3.14159;
							            
	        double triangulo = (a * c) / 2;	
		double circulo = (Math.pow(c, 2) * PI);
	        double trapezio = ((a + b) * c) / 2;	
		double quadrado = Math.pow(b, 2);
		double retangulo = a * b;
												            

		String saidaTriangulo = String.format("TRIANGULO: %.3f", triangulo);

		String saidaCirculo = String.format("CIRCULO: %.3f", circulo);

		String saidaTrapezio = String.format("TRAPEZIO: %.3f", trapezio);

		String saidaQuadrado = String.format("QUADRADO: %.3f", quadrado);

		String saidaRetangulo = String.format("RETANGULO: %.3f", retangulo);


		
		System.out.println(saidaTriangulo);
		System.out.println(saidaCirculo);
		System.out.println(saidaTrapezio);
		System.out.println(saidaQuadrado);
		System.out.println(saidaRetangulo);													        }
}

