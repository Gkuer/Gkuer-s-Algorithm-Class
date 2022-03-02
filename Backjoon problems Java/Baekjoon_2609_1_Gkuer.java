import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.close();

        if (n > m) {
            int tempN = n;
            n = m;
            m = tempN;
        }
        int N = n;
        int M = m;

        while (n%m != 0) {
            int tempN = n;
            n = m;
            m = tempN % m;
        }

        System.out.println(m);
        System.out.println(N*M/m);
    }
}

// Pass