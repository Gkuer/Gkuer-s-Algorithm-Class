import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = 1000 - sc.nextInt();
        int [] coins = {500,100,50,10,5,1};
        int ans = 0;

        for (int coin:coins) {
            while (n >= coin) {
                n -= coin;
                ans += 1;
            }
        }

        System.out.println(ans);
    }
}

// Pass