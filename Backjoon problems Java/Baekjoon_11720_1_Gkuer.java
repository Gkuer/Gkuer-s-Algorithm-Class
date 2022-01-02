import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		String data = sc.next();

		int sm = 0;
		for (int i=0; i<n; i++) {
			sm += data.charAt(i) - '0';
		}

		System.out.println(sm);
	}
}

// Pass