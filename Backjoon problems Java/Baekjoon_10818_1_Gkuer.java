import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int mn = 1000000;
        int mx = -1000000;

        for (int i=0; i<n; i++) {

            int a = sc.nextInt();

            if (mn > a) {
                mn = a;
            }

            if (mx < a) {
                mx = a;
            }
        }

        System.out.println(mn + " " + mx);
    }
}

// Pass