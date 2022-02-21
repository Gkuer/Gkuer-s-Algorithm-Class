import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        int now = 1;
        while (n > 0) {
            if (Integer.toString(now).contains("666")) {
                n -= 1;
            }
            now += 1;
        }

        System.out.println(now-1);

    }
}

// Pass