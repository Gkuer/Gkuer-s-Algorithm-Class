import java.util.Scanner;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String n = sc.next();
            if (n.equals("0")) {
                break;
            }

            String [] origin = new String [n.length()];
            String [] reverse = new String [n.length()];

            for (int i=0;i<n.length();i++) {
                origin[i] = n.substring(i,i+1);
                reverse[n.length()-i-1] = n.substring(i,i+1);
            }

            if (Arrays.equals(origin,reverse)) {
                System.out.println("yes");
            }
            else {
                System.out.println("no");
            }

        }
    }
}

// Pass