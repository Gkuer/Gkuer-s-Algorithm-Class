import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        Queue<Integer> q = new LinkedList<>();

        for (int i=1; i<=n; i++) {
            q.offer(i);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("<");

        while (q.size() > 0) {

            for (int i=1; i<k; i++) {
                q.offer(q.poll());
            }

            if (q.size() != 1) {
                sb.append(q.poll() + ", ");
            } else {
                sb.append(q.poll());
            }
        }

        sb.append(">");

        System.out.println(sb);
    }

}

// Pass