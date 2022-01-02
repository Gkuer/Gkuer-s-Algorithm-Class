import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] alphabets = new int[26];
        for (int i=0; i<26; i++) {
            alphabets[i] = -1;
        }

        String data = sc.nextLine();

        for (int i=0; i<data.length(); i++) {
            if (alphabets[data.charAt(i)-'a'] == -1) {
                alphabets[data.charAt(i) -'a'] = i;
            }
        }

        for (int alphabet : alphabets) {
            System.out.print(alphabet + " ");
        }

    }
}

// Pass