import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
      w
        HashSet<Character> charSet = new HashSet<>();
        int start = 0;  
        int maxLength = 0;  
        
      
        for (int end = 0; end < s.length(); end++) {
           
            while (charSet.contains(s.charAt(end))) {
                charSet.remove(s.charAt(start)); 
                start++; 
            }
            
    
            charSet.add(s.charAt(end));
            
         
            maxLength = Math.max(maxLength, end - start + 1);
        }
        
        return maxLength;
    }
}
