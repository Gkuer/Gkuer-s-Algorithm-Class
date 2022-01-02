import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int first = sc.nextInt();
		int second = sc.nextInt();

		String status = "";
		if (first < second) {
			status = "ascending";
		}
		else {
			status = "descending";
		}
		int val = second;

		for (int i=0; i<6; i++) {
			int n = sc.nextInt();
			String now;
			if (n > val) {
				now = "ascending";
			}
			else {
				now = "descending";
			}

			if (now == status) {
				val = n;
			}
			else {
				status = "mixed";
				break;
			}
		}

		System.out.println(status);
	}
}

// Pass