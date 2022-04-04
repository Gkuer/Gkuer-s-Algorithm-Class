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

        int ans = 0;
        for (int i = 1; i < n+1; i++) {
            String temp = String.valueOf(i);

            if (temp.length() <= 1) {
                ans += 1;
            } else {
                int ini = (temp.charAt(1) - 0) - (temp.charAt(0) - 0);
                boolean flag = true;
                for (int j = 1; j < temp.length()-1; j++) {
                    if ((temp.charAt(j + 1) - 0) - (temp.charAt(j) - 0) != ini) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    ans += 1;
                }
            }
        }

        bw.write(ans +"");
        bw.flush();
    }
}

// Pass