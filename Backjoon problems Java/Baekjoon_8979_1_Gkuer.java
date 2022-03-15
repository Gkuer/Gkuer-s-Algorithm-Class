import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        Long[] maps = new Long[n+1];

        for (int i = 0; i < n; i++) {
            String[] data = br.readLine().split(" ");
            int a = Integer.parseInt(data[0]);
            Long b = Long.valueOf(data[1]);
            Long c = Long.valueOf(data[2]);
            Long d = Long.valueOf(data[3]);

            maps[a] = b * 1000000000001L + c * 1000001 + d;
        }

        Long goal = maps[k];
        int ans = 1;
        for (int i = 1; i < n+1; i++) {
            if (maps[i] > goal) {
                ans += 1;
            }
        }

        bw.write(String.valueOf(ans));
        bw.flush();
    }
}

// Pass