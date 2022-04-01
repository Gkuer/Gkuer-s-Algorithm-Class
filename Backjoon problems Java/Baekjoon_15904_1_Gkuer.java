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

        String[] maps = br.readLine().split("");
        String[] temps = {"U", "C", "P", "C"};
        int temps_s = 0;

        int s = 0;
        int e = maps.length;
        boolean flag = false;
        while (s<e) {
            if (maps[s].equals(temps[temps_s])) {
                temps_s += 1;
                if (temps_s >= 4) {
                    flag = true;
                    break;
                }
            }
            s += 1;
        }

        if (flag) {
            bw.write("I love UCPC");
        } else {
            bw.write("I hate UCPC");
        }

        bw.flush();

    }
}

// Pass