import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int start = 1;
        int end = 1;
        int increase = 1;

        while (!(start <= n && n <= end)) {
            start = end + 1;
            end = end + 6*increase;
            increase += 1;
        }

        System.out.println(increase);
    }
}

// Pass