import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList maps = new ArrayList<Integer>();
        String next = sc.next();
        for (int i = 0; i < next.length(); i++) {
            maps.add(next.charAt(i) - '0');
        }

        maps.sort(Comparator.reverseOrder());

        for (int i = 0; i < maps.size(); i++) {
            System.out.print(maps.get(i));
        }
    }
}

// Pass