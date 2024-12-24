//QUESTÃO 1014 - Consumo

import java.io.IOException;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		            
 	        int distancia = sc.nextInt();
	        double combustivelGasto = sc.nextDouble();
					            
 	        double consumo = distancia / combustivelGasto;
						            
	        String saida = String.format("%.3f km/l", consumo);
							            
	        System.out.println(saida);	
	}
}
