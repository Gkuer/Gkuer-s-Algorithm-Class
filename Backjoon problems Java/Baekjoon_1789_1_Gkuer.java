import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        long n = sc.nextLong();
        long s = 1;
        while ((s*(s-1))/2 <= n) {
            s += 1;
        }
        System.out.println(s-2);
    }
}

// Pass