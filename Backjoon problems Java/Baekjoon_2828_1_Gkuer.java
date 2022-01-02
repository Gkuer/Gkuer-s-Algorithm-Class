import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int j = sc.nextInt();

        int front = 1;
        int end = m;

        int ans = 0;
        for (int i=0; i<j; i++) {
            int apple = sc.nextInt();
            if (apple > end) {
                int temp = apple - end;
                ans += temp;
                front += temp;
                end += temp;
            }
            else if (apple < front) {
                int temp = front - apple;
                ans += temp;
                front -= temp;
                end -= temp;
            }
        }

        System.out.println(ans);

    }
}

// Pass