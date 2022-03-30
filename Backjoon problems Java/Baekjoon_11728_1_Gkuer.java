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

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        int[] maps = new int[n+m];

        StringTokenizer nSt = new StringTokenizer(br.readLine());
        StringTokenizer mSt = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            maps[i] = Integer.parseInt(nSt.nextToken());
        }

        for (int i = 0; i < m; i++) {
            maps[n + i] = Integer.parseInt(mSt.nextToken());
        }

        Arrays.sort(maps);
        for (int i = 0; i < n + m; i++) {
            bw.write(maps[i] + " ");
        }

        bw.flush();
    }
}

// Pass