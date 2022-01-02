import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int ans = 0;
        int pos = 1;
        while (pos <= n) {
            if (n % pos == 0) {
                k -= 1;
                if (k == 0) {
                    ans = pos;
                    break;
                }
            }
            pos += 1;
        }

        System.out.println(ans);
    }
}

// Pass