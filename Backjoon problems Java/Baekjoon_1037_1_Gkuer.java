import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] maps = new int[n];

        for(int i=0; i<n; i++) {
            maps[i] = sc.nextInt();
        }
        sc.close();

        Arrays.sort(maps);

        System.out.println(maps[0]*maps[n-1]);
    }

}

// Pass