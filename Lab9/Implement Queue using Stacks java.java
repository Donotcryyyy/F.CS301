import java.util.Stack;

class MyQueue {
    private Stack<Integer> stackIn; 
    private Stack<Integer> stackOut;
    
    public MyQueue() {
        stackIn = new Stack<>();
        stackOut = new Stack<>();
    }
    
    
    public void push(int x) {
        stackIn.push(x);
    }
    
   
    public int pop() {
       
        if (stackOut.isEmpty()) {
            while (!stackIn.isEmpty()) {
                stackOut.push(stackIn.pop());
            }
        }
        return stackOut.pop();
    }
    
    
    public int peek() {
        
        if (stackOut.isEmpty()) {
            while (!stackIn.isEmpty()) {
                stackOut.push(stackIn.pop());
            }
        }
        return stackOut.peek();
    }
    
 
    public boolean empty() {
        return stackIn.isEmpty() && stackOut.isEmpty();
    }
}


public class Main {
    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); 
        myQueue.push(2); 
        System.out.println(myQueue.peek()); 
        System.out.println(myQueue.pop());  
        System.out.println(myQueue.empty()); 
    }
}
