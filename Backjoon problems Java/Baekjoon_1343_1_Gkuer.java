import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String maps = sc.next();
        maps = maps.replace("XXXX", "AAAA");
        maps = maps.replace("XX", "BB");

        Boolean flag = false;
        for (int i = 0; i < maps.length(); i++) {
            if (maps.charAt(i) == 'X') {
                flag = true;
            }
        }

        if (flag) {
            System.out.println(-1);
        } else {
            System.out.println(maps);
        }
    }

}

// Pass