import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int n = sc.nextInt();

        int ans = 0;
        for (int i=0;i<=n/a+1;i++) {
            for (int j=0;j<=n/b+1;j++) {
                for (int k=0;k<=n/c+1;k++) {
                    if (a*i + b*j + c*k == n) {
                        ans = 1;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}

// Pass