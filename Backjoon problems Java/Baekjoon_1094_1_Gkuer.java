import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int sm = 64;
        int mn = 64;
        int cnt = 1;

        while (sm != x) {
            int mn_half = mn / 2;

            if (sm-mn_half >= x) {
                mn /= 2;
                sm -= mn_half;
            } else {
                cnt += 1;
                mn /= 2;
            }
        }

        System.out.println(cnt);
    }

}

// Pass