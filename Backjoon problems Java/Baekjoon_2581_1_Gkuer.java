import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.close();

        ArrayList<Integer> maps = new ArrayList<>();

        maps.add(2);
        maps.add(3);

        for (int i = 4; i < 15000; i++) {
            boolean flag = false;
            for (int map:maps) {
                if (i % map == 0) {
                    flag = true;
                    break;
                }
            }

            if (!flag) {
                maps.add(i);
            }
        }

        int mn_ans = 0;
        int sm_ans = 0;
        boolean check_flag = false;
        for (int i = 0; i < maps.size(); i++) {
            int res = maps.get(i);
            if (n <= res && res <= m) {
                if (!check_flag) {
                    mn_ans = res;
                    sm_ans += res;
                    check_flag = true;
                } else {
                    sm_ans += res;
                }
            }
        }

        if (mn_ans == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sm_ans);
            System.out.println(mn_ans);
        }
    }
}

// Pass