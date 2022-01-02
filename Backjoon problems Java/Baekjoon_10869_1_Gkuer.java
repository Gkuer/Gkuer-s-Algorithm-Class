import java.util.Scanner;
public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		sc.close();
		
		int ans1 = n1 + n2;
		int ans2 = n1 - n2;
		int ans3 = n1 * n2;
		int ans4 = n1 / n2;
		int ans5 = n1 % n2;
		
		System.out.println(ans1);
		System.out.println(ans2);
		System.out.println(ans3);
		System.out.println(ans4);
		System.out.println(ans5);
		
	}

}

// Pass