import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        sc.close();

        int[] cnts = new int[2];
        int start = 0;

        while (start <  s.length()) {
            while ((start < s.length()-1) && (s.charAt(start) == s.charAt(start+1))) {
                start += 1;
            }

            cnts[s.charAt(start) - '0'] += 1;
            start += 1;
        }

        System.out.println(Math.min(cnts[0],cnts[1]));
    }
}

// Pass