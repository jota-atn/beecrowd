//QUESTÃO 1015 - Distância entre dois Pontos

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
 	        Scanner sc = new Scanner(System.in);
			            
	        double x1 = sc.nextDouble();
	        double y1 = sc.nextDouble();
					            
 	        double x2 = sc.nextDouble();
	        double y2 = sc.nextDouble();
							            
		double distancia = Math.sqrt((Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2)));
								     
	    	String saida = String.format("%.4f", distancia);
	        System.out.println(saida);
 		sc.close();
	}
}

