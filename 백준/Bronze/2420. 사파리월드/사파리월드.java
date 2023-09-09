import java.util.Scanner;
import java.math.BigInteger;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextInt();
		long b = sc.nextInt();
		
		if(a>b) {
			System.out.println(a-b);
		}
		else {
			System.out.println(b-a);
		}
		
	}
	

}
