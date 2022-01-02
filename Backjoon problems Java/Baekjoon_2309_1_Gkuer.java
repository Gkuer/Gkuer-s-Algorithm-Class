import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
	public static ArrayList<Integer> ans = new ArrayList<Integer>();
	public static int [] temps = new int [9]; // array
	public static int [] maps = new int [9];
	public static int bf(int k, int sm) {
		if (sm > 100) {
			return 0;
		}
		if (k == 7) {
			if (sm == 100) {
				for (int j=0;j<9;j++) {
					if (temps[j] == 1) {
						ans.add(maps[j]);
					}
				}
				return 1;
			}
			return 0;
		}

		for (int i=0;i<9;i++) {
			if (temps[i] == 0) {
				temps[i] = 1;
				if (bf(k+1,sm+maps[i]) == 1) {
					return 1;
				}
				temps[i] = 0;
			}
		}

		return 0;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);


		for (int i=0; i<9; i++) {
			maps[i] = sc.nextInt();
		}


		for (int i=0; i<9; i++) {
			temps[i] = 0;
		}

		bf(0,0);

		Collections.sort(ans);

		for (int i=0; i<7; i++) {
			System.out.println(ans.get(i));
		}


	}
}

// Pass