import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for (int i=0;i<t;i++) {
			int c = sc.nextInt();

			int quater = c/25;
			c = c%25;

			int dime = c/10;
			c = c%10;

			int nickel = c/5;
			c = c%5;

			int penny = c;

			System.out.println(quater + " " + dime + " " + nickel + " " + penny);

		}
	}
}

// Pass