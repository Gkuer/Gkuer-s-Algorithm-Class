import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int j = sc.nextInt();

        int start = 1;
        int end = m;
        int cnt = 0;

        for (int i = 0; i < j; i++) {
            int val = sc.nextInt();

            if (start <= val && val <= end) {
                continue;
            } else if (start > val) {
                cnt += start - val;
                start = val;
                end = start + m - 1;
            } else if (end < val) {
                cnt += val - end;
                end = val;
                start = end - m + 1;
            }
        }
        sc.close();

        System.out.println(cnt);

    }
}

// Pass