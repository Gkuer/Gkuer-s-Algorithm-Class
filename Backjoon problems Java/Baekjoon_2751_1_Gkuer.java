import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();

        ArrayList<Integer> maps = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            maps.add(sc.nextInt());
        }
        sc.close();

        Collections.sort(maps);

        for (int map:maps) {
            sb.append(map).append('\n');
        }
        System.out.println(sb);
    }
}

// Pass