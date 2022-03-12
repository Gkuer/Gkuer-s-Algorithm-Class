import java.sql.Array;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[][] maps = new int[n][2];

        for (int i = 0; i < n; i++) {
            int height = sc.nextInt();
            int weight = sc.nextInt();
            maps[i][0] = height;
            maps[i][1] = weight;
        }

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int bigger = 0;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (maps[i][0] < maps[j][0] && maps[i][1] < maps[j][1]) {
                        bigger += 1;
                    }
                }
            }

            ans[i] = bigger + 1;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}

// Pass