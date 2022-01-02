import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if (a==0 && b==0 && c==0) {
                break;
            }

            a = (int) Math.pow(a,2);
            b = (int) Math.pow(b,2);
            c = (int) Math.pow(c,2);

            if (a+b==c || a+c==b || b+c==a) {
                System.out.println("right");
            }
            else {
                System.out.println("wrong");
            }
        }
    }
}

// Pass