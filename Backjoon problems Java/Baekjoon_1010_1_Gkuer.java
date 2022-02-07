import java.util.Scanner;
public class Main {

	private static double factorial(double x) {
		if (x <= 1) {
			return 1;
		}

		return x * factorial(x - 1);
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int tc = 0; tc < t; tc++) {
			double n = sc.nextInt();
			double m = sc.nextInt();
			System.out.printf("%.0f\n",(factorial(m) / (factorial(m-n) * factorial(n))));
		}

		sc.close();
	}

}

// Pass