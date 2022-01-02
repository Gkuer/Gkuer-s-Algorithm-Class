import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			int h = sc.nextInt();
			int w = sc.nextInt();
			int m = sc.nextInt();

			int floor = m % h;
			int dist;
			if (floor == 0) {
				floor = h;
				dist = (m / h);
			}
			else {
				dist = (m / h) + 1;
			}

			System.out.println(floor*100+dist);
		}
	}
}

// Pass