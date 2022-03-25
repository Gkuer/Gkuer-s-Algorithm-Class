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
            maps[i][0] = Integer.parseInt(temps[0]);
            maps[i][1] = Integer.parseInt(temps[1]);
        }

        Arrays.sort(maps,(e1,e2) -> {
            if (e1[1] == e2[1]) {
                return e1[0] - e2[0];
            } else {
                return e1[1] - e2[1];
            }
        });

        for (int i = 0; i < n; i++) {
            bw.write(maps[i][0] + " " + maps[i][1] + "\n");
        }

        bw.flush();
    }
}

// Pass