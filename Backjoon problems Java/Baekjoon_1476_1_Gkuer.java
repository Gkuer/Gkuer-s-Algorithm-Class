import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] goal = new int[3];
        for (int i = 0; i < 3; i++) {
            goal[i] = sc.nextInt();
        }
        sc.close();

        int[] maps = new int[3];
        for (int i = 0; i < 3; i++) {
            maps[i] = 0;
        }

        int[] limit = new int[3];
        limit[0] = 15;
        limit[1] = 28;
        limit[2] = 19;

        int cnt = 0;
        while (true) {

            int tempCnt = 0;
            for (int i = 0; i < 3; i++) {
                if (maps[i] == goal[i]) {
                    tempCnt += 1;
                }
            }
            if (tempCnt == 3) {
                break;
            }

            for (int i = 0; i < 3; i++) {
                maps[i] += 1;
            }

            for (int i = 0; i < 3; i++) {
                if (maps[i] > limit[i]) {
                    maps[i] = 1;
                }
            }

            cnt += 1;
        }

        System.out.println(cnt);
    }
}

// Pass