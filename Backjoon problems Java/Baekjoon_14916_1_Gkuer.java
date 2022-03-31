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

        int n = Integer.parseInt(br.readLine());
        int inf = 987654321;
        int[] temps = {0, inf, 1, inf, 2, 1};
        int[] maps = new int[n+1];

        if (n <= 5) {
            for (int i = 1; i < n+1; i++) {
                maps[i] = temps[i];
            }
        } else {
            for (int i = 1; i < 6; i++) {
                maps[i] = temps[i];
            }
        }

        for (int i = 6; i < n+1; i++) {
            maps[i] = Math.min(maps[i - 2], maps[i - 5])+1;
        }

        if (maps[n] >= inf) {
            bw.write(-1 + "");
        } else {
            bw.write(maps[n] +"");
        }

        bw.flush();
    }
}

// Pass