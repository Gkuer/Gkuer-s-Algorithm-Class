import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int ans  = 0;

        int val = 1;
        while (val <= n) {
            int sm = val;

            int temp = val;
            while (temp != 0) {
                sm += temp % 10;
                temp /= 10;
            }

            if (sm == n) {
                ans = val;
                break;
            }

            val += 1;
        }

        System.out.println(ans);
    }
}

// Pass