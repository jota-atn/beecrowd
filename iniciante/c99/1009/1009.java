//QUESTÃO 1009 - Salário com Bônus

import java.io.IOException;
import java.util.Scanner; 

public class Main {
	public static void main(String[] args) throws IOException {
	        Scanner sc = new Scanner(System.in);
			            
	        String nome = sc.next();
	        double salario = sc.nextDouble();
	        double vendas = sc.nextDouble();
						            	
		double salarioFinal = salario + (vendas * 0.15);
							        
		String saida = String.format("TOTAL = R$ %.2f", salarioFinal);
								            						            
		System.out.println(saida);    
	}   
}

