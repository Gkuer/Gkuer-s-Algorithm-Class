import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int testCase = 1;
        while (true) {
            int l = sc.nextInt();
            int p = sc.nextInt();
            int v = sc.nextInt();

            if (l+p+v == 0) {
                break;
            }

            int answer = 0;

            answer += (v / p)*l;
            answer += Math.min(l, v - p*(v / p));

            System.out.printf("Case %s: %s %n",testCase,answer);
            testCase += 1;
        }
        sc.close();
    }
}

// Pass