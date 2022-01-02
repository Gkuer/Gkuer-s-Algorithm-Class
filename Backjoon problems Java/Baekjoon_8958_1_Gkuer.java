import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i=0; i<t; i++) {
            String a = sc.next();

            int res = 0;
            int temp = 0;
            for (int j=0; j<a.length(); j++) {
                if (a.charAt(j) == 'O') {
                    temp += 1;
                    res += temp;
                }
                else {
                    temp = 0;
                }

            }

            System.out.println(res);
        }
    }
}

// Pass