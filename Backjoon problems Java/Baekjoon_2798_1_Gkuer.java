import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int [] cards = new int[n];

        for (int i=0; i<n; i++) {
            int pick = sc.nextInt();
            cards[i] = pick;
        }

        int ans = 0;
        for (int i=0; i<n-2; i++) {
            for (int j=i+1; j<n-1; j++) {
                for (int k=j+1; k<n; k++) {
                    int res = cards[i] + cards[j] + cards[k];
                    if ((res > ans)&&(res<=m)) {
                        ans = res;
                    }
                }
            }
        }

        System.out.println(ans);
    }
}

// Pass