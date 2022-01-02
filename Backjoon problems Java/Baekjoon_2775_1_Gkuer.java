import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		for (int i=0;i<t;i++) {
			int k = sc.nextInt();
			int n = sc.nextInt();
			int [][] dp = new int [k+1][n+1];

			for (int j=0;j<n+1;j++) {
				dp[0][j] = j;
			}

			for (int j=1;j<k+1;j++) {
				for (int l=1;l<n+1;l++) {
					for (int m=1;m<=l;m++) {
						dp[j][l] += dp[j-1][m];
					}
				}
			}

			System.out.println(dp[k][n]);
		}
	}
}

// Pass