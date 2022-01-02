import java.util.Scanner;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int temp = 0;
        int ans = 0;
        for (int i=0; i<10; i++) {
            int a = sc.nextInt();
            temp += a;
            if (Math.abs(100-temp) <= Math.abs(100-ans)) {
                ans = temp;
            }
        }

        System.out.println(ans);
    }
}

// Pass