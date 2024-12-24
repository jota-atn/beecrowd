//QUESTÃO 1011 - Esfera

import java.io.IOException;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) throws IOException {
		     
        	Scanner sc = new Scanner(System.in);
			            
	        double PI = 3.14159;
	        double raio = sc.nextDouble();
					            
 	        double volume = (4.0/3) * PI * Math.pow(raio, 3);
						            
	        String saida = String.format("VOLUME = %.3f", volume);
							        
	        System.out.println(saida);
	}
}
