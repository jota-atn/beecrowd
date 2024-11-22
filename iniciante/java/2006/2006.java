mport java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		            
		Scanner sc = new Scanner(System.in);
			            
		int t = sc.nextInt();
				            
		int[] inputs = new int[5];
					            
		for (int i = 0; i < inputs.length; i++) {
			inputs[i] = sc.nextInt();
		}
						            
		int counter = 0;
							            
		for (int i = 0; i < inputs.length; i++) {
			if (inputs[i] == t) {
				counter++;
			}
		}
								            
		System.out.println(counter);
									            
	}
}
