import java.util.Scanner;

public class Main {
    public static int pactorial(int x) {
        int res = 1;
        for (int i=2; i<=x; i++) {
            res *= i;
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int ans = pactorial(n) / (pactorial(k) * pactorial(n-k));
        System.out.println(ans);
    }
}

// Pass