public class AggregateAnalysis {
    public static double calculateAverageCost(int n) {
        int totalCost = 0;

        for (int i = 1; i <= n; i++) {
            // Хоёрын зэрэгт шалгах
            if ((i & (i - 1)) == 0) {
                totalCost += i; 
            } else {
                totalCost += 1; 
            }
        }

        return (double) totalCost / n;
    }

    public static void main(String[] args) {
        int n = 16;
        System.out.println("Нэгжийн дундаж өртөг: " + calculateAverageCost(n));
    }
}
