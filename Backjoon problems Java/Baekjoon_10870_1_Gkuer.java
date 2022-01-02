import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] pibonacci = new int [21];
        pibonacci[0] = 0;
        pibonacci[1] = 1;

        for (int i=2; i<21; i++) {
            pibonacci[i] = pibonacci[i-2] + pibonacci[i-1];
        }

        int n = sc.nextInt();
        System.out.println(pibonacci[n]);
    }
}

// Pass