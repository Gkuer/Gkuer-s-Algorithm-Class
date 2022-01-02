import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        int cnt = 0;
        int cnt2 = 0;
        int cnt3 = 0;

        while (t >= 300) {
            t -= 300;
            cnt += 1;
        }

        while (t >= 60) {
            t -= 60;
            cnt2 += 1;
        }

        while (t >= 10) {
            t -= 10;
            cnt3 += 1;
        }

        if (t > 0) {
            System.out.println(-1);
        }
        else {
            System.out.print(cnt + " " + cnt2 + " " + cnt3);
        }

        sc.close();
    }
}

// Pass