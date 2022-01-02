import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n =  sc.nextInt();
		int [] dp = new int [n+1];

		for (int i=0; i<n+1; i++) {
			dp[i] = 5001;
		}
		dp[3] = 1;


		if (n<5) {

		}
		else if (n == 5) {
			dp[5] = 1;
		}
		else {
			dp[5] = 1;

			for (int i=6;i<n+1;i++) {
				dp[i] = Math.min(dp[i-5],dp[i-3]);
				if (dp[i] != 5001) {
					dp[i] += 1;
				}
			}
		}
		if (dp[n] == 5001) {
			System.out.println(-1);
		}
		else {
			System.out.println(dp[n]);
		}
	}
}

// Pass