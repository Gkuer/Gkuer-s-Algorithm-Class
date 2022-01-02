import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =  sc.nextInt();
        int sm = 0;
        int mx = 0;
        for (int i=0; i<n; i++) {
            int test = sc.nextInt();
            sm += test;
            if (mx < test) {
                mx = test;
            }
        }

        double res = (double) sm / mx;
        res = res * 100 / n;
        System.out.println(res);
    }
}

// Pass