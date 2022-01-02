import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i=0; i<t; i++) {
            int n = sc.nextInt();
            String data = sc.next();

            for (int j=0; j<data.length(); j++) {
                for (int k=0; k<n; k++) {
                    System.out.print(data.charAt(j));
                }
            }
            System.out.println();
        }
    }
}

// Pass