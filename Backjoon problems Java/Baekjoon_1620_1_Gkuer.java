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

        HashMap<String, Integer> strDict = new HashMap<>();
        HashMap<Integer, String> intDict = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String data = br.readLine();
            strDict.put(data,i+1);
            intDict.put(i + 1, data);
        }

        for (int i = 0; i < m; i++) {
            String des = br.readLine();
            try {
                int intDes = Integer.parseInt(des);
                System.out.println(intDict.get(intDes));
            } catch (NumberFormatException e) {
                System.out.println(strDict.get(des));
            }
        }
    }
}

// Pass