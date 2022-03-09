import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] cro = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};

        String maps = sc.next();
        sc.close();

        for (String data: cro) {
            maps = maps.replace(data, "1");
        }

        System.out.println(maps.length());
    }
}

// Pass