import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int[] maps = new int[10];
            for (int j = 0; j < 10; j++) {
                maps[j] = sc.nextInt();
            }

            Arrays.sort(maps);

            System.out.println(maps[7]);
        }
    }
}

// Pass