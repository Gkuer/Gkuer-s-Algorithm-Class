import java.util.Scanner;
import java.util.Arrays;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int tc=0; tc<t; tc++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            int mn = Math.min(a,b);
            int mx = Math.max(a,b);

            int mndiv = mn;
            while (mndiv > 0) {
                if (a%mndiv == 0 && b%mndiv == 0) {
                    break;
                }
                mndiv -= 1;
            }

            int mxmul = mx;
            while (mxmul <= 1000000) {
                if (mxmul%a == 0 && mxmul%b == 0) {
                    break;
                }
                mxmul += 1;
            }

            System.out.println(Integer.toString(mxmul) + " " + Integer.toString(mndiv));
        }
    }
}

// Pass