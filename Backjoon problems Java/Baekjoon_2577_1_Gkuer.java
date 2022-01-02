import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] nums = new int [10];

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        String res = Integer.toString(a * b * c);

        for (int i=0; i<res.length(); i++) {
            nums[res.charAt(i) - '0'] += 1;
        }

        for (int i=0; i<10; i++) {
            System.out.println(nums[i]);
        }

    }
}

// Pass