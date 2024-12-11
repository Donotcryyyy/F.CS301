import java.util.Stack;

public class FinancialAnalysis {
    static class AutoBackupStack<T> {
        private Stack<T> stack = new Stack<>();
        private Stack<T> backup = new Stack<>();
        private int k; // k тоо бүрт нөөцөлнө
        private int operationCount = 0;

        public AutoBackupStack(int k) {
            this.k = k;
        }

        public void push(T value) {
            stack.push(value);
            operationCount++;
            if (operationCount % k == 0) {
                backup = (Stack<T>) stack.clone();
            }
        }

        public T pop() {
            if (stack.isEmpty()) return null;
            operationCount++;
            if (operationCount % k == 0) {
                backup = (Stack<T>) stack.clone();
            }
            return stack.pop();
        }
    }

    public static void main(String[] args) {
        AutoBackupStack<Integer> stack = new AutoBackupStack<>(3);

        stack.push(1);
        stack.push(2);
        stack.push(3); // Нөөцлөлт энд болно
        stack.push(4);
        stack.pop();
        stack.push(5);
    }
}
