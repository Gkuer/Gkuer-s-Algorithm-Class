import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int n = Integer.parseInt(br.readLine());

        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] data = br.readLine().split(" ");
            String name = data[0];
            String status = data[1];

            if (status.equals("enter")) {
                set.add(name);
            } else {
                set.remove(name);
            }
        }
        List<String> maps = new ArrayList<>();
        Iterator<String> it = set.iterator();
        while (it.hasNext()) {
            maps.add(it.next());
        }

        Collections.sort(maps,Collections.reverseOrder());

        for (String map: maps) {
            bw.write(map + "\n");
        }

        bw.flush();
    }
}

// Pass