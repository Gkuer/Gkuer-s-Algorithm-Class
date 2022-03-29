import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        Boolean[][] maps = new Boolean[n][m];

        for (int i=0; i<n; i++) {
            String data = sc.next();
            for (int j=0; j<m; j++) {
                if (data.charAt(j) == 'W') {
                    maps[i][j] = true;
                } else {
                    maps[i][j] = false;
                }
            }
        }

        int ans = 2500;
        for (int i=0; i<n-7; i++) {
            for (int j=0; j<m-7; j++) {
                int w_cnt = 0;
                int b_cnt = 0;

                for (int k=0; k<8; k++) {
                    for (int l=0; l<8; l++) {
                        if ((k+l) % 2 == 0) {
                            if (maps[i+k][j+l]) {
                                w_cnt += 1;
                            }
                            if (!maps[i+k][j+l]) {
                                b_cnt += 1;
                            }
                        } else {
                            if (maps[i+k][j+l]) {
                                b_cnt += 1;
                            }
                            if (!maps[i+k][j+l]) {
                                w_cnt += 1;
                            }
                        }
                    }
                }

                if (ans > w_cnt) {
                    ans = w_cnt;
                }
                if (ans > b_cnt) {
                    ans = b_cnt;
                }
            }
        }

        System.out.println(ans);
    }

}

// Pass