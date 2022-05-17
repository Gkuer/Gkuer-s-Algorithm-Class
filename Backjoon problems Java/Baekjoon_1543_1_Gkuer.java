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

        String txt = br.readLine();
        String kyword = br.readLine();

        String replaceTxt = txt.replace(kyword, "_");
        int ans = 0;
        for (int i = 0; i < replaceTxt.length(); i++) {
            if (replaceTxt.charAt(i) == '_') {
                ans += 1;
            };
        }

        bw.write(ans + "");
        bw.flush();
    }
}

// Pass