import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] maps = new int [27];

        for (int i=0; i<27; i++) {
            maps[i] = 0;
        }

        String data = sc.next();
        for (int i=0; i<data.length(); i++) {
            if ('A' <= data.charAt(i) && data.charAt(i) < 'a') {
                maps[data.charAt(i)-'A'] += 1;
            }
            else {
                maps[data.charAt(i)-'a'] += 1;
            }
        }

        int mx = 0;
        int mx_alpha = 0;
        boolean overlap = false;
        for (int i=0; i<27; i++) {
            if (mx < maps[i]) {
                mx = maps[i];
                mx_alpha = i;
                overlap = false;
            }
            else if (mx==maps[i]) {
                overlap = true;
            }
        }

        if (overlap) {
            System.out.println("?");
        }
        else {
            char res = (char) (mx_alpha+'A');
            System.out.println(res);
        }
    }
}

// Pass