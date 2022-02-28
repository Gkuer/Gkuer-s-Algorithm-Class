import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int A = a;
            int B = b;

            while (a % b != 0) {
                int tempA = a;
                a = b;
                b = tempA%b;
            }

            System.out.println(A*B/b);
        }
    }
}

// Pass