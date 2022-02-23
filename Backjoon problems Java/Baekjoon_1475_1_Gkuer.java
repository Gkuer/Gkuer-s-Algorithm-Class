import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String n = sc.next();
        sc.close();

        int[] maps = new int[10];
        for (int i = 0; i < 10; i++) {
            maps[i] = 0;
        }

        for (int i = 0; i < n.length(); i++) {
            if (n.charAt(i) != '6' && n.charAt(i) != '9') {
                maps[n.charAt(i)-'0'] += 1;
            } else {
                if (maps[6] < maps[9]) {
                    maps[6] += 1;
                } else {
                    maps[9] += 1;
                }
            }
        }

        System.out.println(Arrays.stream(maps).max().getAsInt());
    }
}

// Pass