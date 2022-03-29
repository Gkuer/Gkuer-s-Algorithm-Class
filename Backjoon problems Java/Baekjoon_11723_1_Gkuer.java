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
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        ArrayList<String> maps = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String program;
            String data;

            String command = br.readLine();
            if (!(command.equals("all") || (command.equals("empty")))) {
                String[] listCommand = command.split(" ");
                program = listCommand[0];
                data = listCommand[1];

                if (program.equals("add")) {
                    if (!maps.contains(data)) {
                        maps.add(data);
                    }
                } else if (program.equals("remove")) {
                    if (maps.contains(data)) {
                        maps.remove(data);
                    }
                } else if (program.equals("check")) {
                    if (maps.contains(data)) {
                        bw.write(1 + "\n");
                    } else {
                        bw.write(0 + "\n");
                    }
                } else if (program.equals("toggle")) {
                    if (maps.contains(data)) {
                        maps.remove(data);
                    } else {
                        maps.add(data);
                    }
                }
            } else {
                if (command.equals("all")) {
                    maps = new ArrayList<>();
                    for (int j = 1; j < 21; j++) {
                        maps.add(String.valueOf(j));
                    }
                } else {
                    maps = new ArrayList<>();
                }
            }
        }

        bw.flush();
    }
}

// Pass