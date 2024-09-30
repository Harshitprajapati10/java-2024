public class HappyNo{

    static int findSquare(int number){
        int ans = 0;
        while (number > 0){
            int rem = number % 10;
            ans += rem * rem;
            number /= 10;
        }return ans;
    }

    static boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        do {
            slow = findSquare(slow);
            fast = findSquare(findSquare(fast));
        } while (slow != fast);
        return slow == 1;
    }
    public static void main(String[] args) {
        boolean a = isHappy(19);
        System.out.println(a);
    }
}