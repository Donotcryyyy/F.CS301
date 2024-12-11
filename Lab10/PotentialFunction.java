public class PotentialFunction {
    public static int calculatePotentialCost(int[] D) {
        int totalCost = 0;
        int potential = 0;

        for (int i = 0; i < D.length; i++) {
            totalCost += D[i]; // Үйлдлийн өртөг нэмэх
            potential += Math.max(D[i], 0); // Потенциал функц шинэчлэл
        }

        return totalCost + potential;
    }

    public static void main(String[] args) {
        int[] operations = {1, -2, 3, -1, 4}; // Туршилтын өгөгдөл
        System.out.println("Нийт өртөг: " + calculatePotentialCost(operations));
    }
}
