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

        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);

        LinkedList<Integer> maps = new LinkedList<>();
        for (int i = 1; i < n + 1; i++) {
            maps.offer(i);
        }

        int cnt = 0;
        StringBuffer sb = new StringBuffer();
        sb.append("<");
        while (maps.size() >= 2) {
            cnt += 1;
            Integer val = maps.poll();
            if (cnt % m == 0) {
                sb.append(String.valueOf(val) + ", ");
            } else {
                maps.offer(val);
            }
        }

        sb.append(maps.poll() + ">");

        bw.write(sb.toString());
        bw.flush();
    }
}

// Pass