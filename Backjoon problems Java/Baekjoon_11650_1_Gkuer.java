import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] maps = new int[n][2];

        for (int i = 0; i < n; i++) {
            String[] temps = br.readLine().split(" ");
            int a = Integer.parseInt(temps[0]);
            int b = Integer.parseInt(temps[1]);
            maps[i][0] = a;
            maps[i][1] = b;
        }

        Arrays.sort(maps, (e1,e2) -> {
            if (e1[0] == e2[0]) {
                return e1[1] - e2[1];
            } else {
                return e1[0] - e2[0];
            }
        });

        for (int i = 0; i < n; i++) {
            bw.write(maps[i][0] + " " + maps[i][1] + "\n");
        }

        bw.flush();
    }
}

// Pass