import java.util.*;

public class Main {

    public static void main(String[] args) {

        ArrayList<Integer> maps = new ArrayList<>();

        for (int i = 1; i < 10001; i++) {
            int sm = i;
            for (int j = 0; j < Integer.toString(i).length(); j++) {
                sm += Integer.toString(i).charAt(j) - '0';
            }
            maps.add(sm);
        }

        for (int i = 1; i < 10001; i++) {
            if (!maps.contains(i)) {
                System.out.println(i);
            }
        }
    }
}

// Pass