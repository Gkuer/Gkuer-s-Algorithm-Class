import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int v = sc.nextInt();

		int res =  (v-b) / (a-b);
		int ans = ((v-b) % (a-b) > 0) ? res+1:res;
		System.out.println(ans);
	}
}

// Pass