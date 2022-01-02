import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String data = sc.next();
        data = data.replace("LL","S");

        if (data.length()+1 > n) {
            System.out.println(n);
        }
        else {
            System.out.println(data.length() + 1);
        }
    }
}

// Pass