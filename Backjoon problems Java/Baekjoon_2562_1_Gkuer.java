import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int mx = 0;
		int mx_idx = 0;
		for (int i=1; i<10; i++) {
			int a = sc.nextInt();
			if (mx < a) {
				mx = a;
				mx_idx=i;
			}
		}

		System.out.println(mx);
		System.out.println(mx_idx);
	}
}

// Pass