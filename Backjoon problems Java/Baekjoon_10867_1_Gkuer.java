import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class Main {

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());

		String[] maps = br.readLine().split(" ");
		ArrayList<Integer> temps = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			int data = Integer.parseInt(maps[i]);
			if (!temps.contains(data)) {
				temps.add(data);
			}
		}

		Collections.sort(temps);

		for (int i = 0; i < temps.size(); i++) {
			bw.write(temps.get(i) + " ");
		}

		bw.flush();
	}
}

// Pass