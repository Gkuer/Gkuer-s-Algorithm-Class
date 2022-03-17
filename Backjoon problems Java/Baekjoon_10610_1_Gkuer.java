import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String n = br.readLine();

        int sm = 0;
        for (int i = 0; i < n.length(); i++) {
            sm += n.charAt(i) - '0';
        }

        if (sm % 3 != 0 || !n.contains("0")) {
            System.out.println(-1);
        } else {
            char[] maps = n.toCharArray();
            Arrays.sort(maps);

            char[] answer = new char[maps.length];
            for (int i = 0; i < maps.length; i++) {
                answer[i] = maps[maps.length - i - 1];
            }

            for (int i = 0; i < maps.length; i++) {
                bw.write(answer[i]);
            }
        }

        bw.flush();
    }
}

// Pass