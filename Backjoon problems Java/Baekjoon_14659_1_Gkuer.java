import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =  sc.nextInt();
        int ans = 0;
        int temp = sc.nextInt();
        int cnt = 0;

        for (int i=1; i<n; i++) {
            int a = sc.nextInt();
            if (temp > a) {
                cnt += 1;
            }
            else {
                if (ans < cnt) {
                    ans = cnt;
                }
                temp = a;
                cnt = 0;
            }
        }

        if (cnt>0) {
            if (ans < cnt) {
                ans = cnt;
            }
        }

        System.out.println(ans);
    }
}

// Pass