import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		String data = sc.next();
		long sm = 0;
		long pow = 1;
		for (int i=0; i<n; i++) {
			sm += ((data.charAt(i) - 'a' + 1) * pow);
			pow = (31*pow)%1234567891;
		}

		System.out.println(sm%1234567891);

	}
}

// Pass