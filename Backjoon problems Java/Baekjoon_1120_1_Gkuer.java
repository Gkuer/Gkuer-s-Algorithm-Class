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
        String a = input[0];
        String b = input[1];

        int ans = 0;
        for (int i = 0; i < b.length()-a.length()+1; i++) {
            String temp_b = "";
            for (int j = 0; j < a.length(); j++) {
                temp_b += b.charAt(i+j);
            }

            int cnt = 0;
            for (int j = 0; j < a.length(); j++) {
                if (temp_b.charAt(j) == a.charAt(j)) {
                    cnt += 1;
                }
            }

            ans = Math.max(ans, cnt);
        }

        bw.write(String.valueOf(a.length()-ans));
        bw.flush();
    }
}

// Pass