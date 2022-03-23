import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] maps = new int[n];
        for (int i = 0; i < n; i++) {
            maps[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(maps);

        for (int i = 0; i < n; i++) {
            bw.write(maps[i] + "\n");
        }

        bw.flush();
    }
}

// Pass