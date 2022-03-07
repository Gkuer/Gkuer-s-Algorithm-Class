import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[] maps = new int[8];
        int[] origin = new int[8];
        
        for (int i = 0; i < 8; i++) {
            int val = sc.nextInt();
            maps[i] = val;
            origin[i] = val;
        }
        sc.close();
        
        Arrays.sort(maps);
        int[] ans = new int[5];
        for (int i = 3; i < 8; i++) {
            ans[i - 3] = maps[i];
        }

        int sm = 0;
        int[] lst = new int[8];
        for (int i = 0; i < 8; i++) {
            int data = origin[i];
            boolean res = Arrays.stream(ans).anyMatch(x -> x == data);
            if (res) {
                sm += origin[i];
                lst[i] = 1;
            }
        }

        System.out.println(sm);

        int cnt = 0;
        for (int i = 0; i < 8; i++) {
            if (lst[i] == 1) {
                if (cnt <= 3) {
                    System.out.print(Integer.toString(i+1) + " ");
                    cnt += 1;
                } else {
                    System.out.print(Integer.toString(i+1));
                }
            }
        }
    }
}

// Pass