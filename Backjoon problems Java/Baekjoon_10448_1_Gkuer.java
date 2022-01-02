import java.util.Scanner;
import java.util.ArrayList;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		ArrayList<Integer> maps = new ArrayList<Integer>();

		int val = 1;
		int cnt = 2;

		while (val < 1000) {
			maps.add(val);
			val += cnt;
			cnt += 1;
		}

		int t = sc.nextInt();
		for (int tc=0; tc<t; tc++) {
			int n = sc.nextInt();
			int ans = 0;
			for (int i=0;i<maps.size();i++) {
				for (int j=i; j<maps.size();j++) {
					for (int k=j; k<maps.size();k++) {
						if (maps.get(i) + maps.get(j) + maps.get(k) == n) {
							ans = 1;
						}
					}
				}
			}
			System.out.println(ans);
		}
	}
}

// Pass