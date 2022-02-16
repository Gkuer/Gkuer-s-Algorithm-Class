import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int ans = 0;
        for (int i = 0; i < n; i++) {
            String data = sc.next();
            String maps = "";
            Boolean flag = false;
            for (int j = 0; j < data.length()-1; j++) {
                if (data.charAt(j) == data.charAt(j+1)) {
                    continue;
                } else {
                    if (maps.contains(Character.toString(data.charAt(j)))) {
                        flag = true;
                        break;
                    } else {
                        maps += Character.toString(data.charAt(j));
                    }
                }
            }
            if (!flag) {
              if (!maps.contains(data.substring(data.length()-1))) {
                  ans += 1;
              }
            }
        }

        System.out.println(ans);
    }

}

// Pass