//QUESTÃO 1008 - Salário


import java.io.IOException;
import java.util.Scanner;

public class Main { 
	public static void main(String[] args) throws IOException {
  	        Scanner sc = new Scanner(System.in);
			            
		int idFuncionario = sc.nextInt();
	        int horasTrabalhadas = sc.nextInt();
		double valorHora = sc.nextDouble();
						            
		double salario = horasTrabalhadas * valorHora;
							            
		String saida = String.format("NUMBER = %d\nSALARY = U$ %.2f", idFuncionario, salario);
								            
		System.out.println(saida);
	}
}

