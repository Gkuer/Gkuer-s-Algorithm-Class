import java.util.Scanner;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int [] people = new int [9];
		for (int i=0; i<9; i++) {
			people[i] = sc.nextInt();
		}

		int sm = Arrays.stream(people).sum();
		for (int i=0; i<8; i++) {
			for (int j=i+1; j<9; j++) {
				if (sm - people[i] - people[j] == 100) {
					for (int k=0; k<9; k++) {
						if (k != i && k != j) {
							System.out.println(people[k]);
						}
					}
				}
			}
		}

	}
}

// Pass