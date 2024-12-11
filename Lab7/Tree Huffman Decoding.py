import queue as Queue

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

   
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.data < other.data

def huffman_hidden(freq):

    q = Queue.PriorityQueue()

   
    for key in freq:
        q.put(Node(freq[key], key))
    

    while q.qsize() > 1:
       
        a = q.get()
        b = q.get()
        
        
        obj = Node(a.freq + b.freq, '\0')  
        obj.left = a
        obj.right = b
        
       
        q.put(obj)
    

    return q.get()

def decodeHuff(root, s):
  
    current_node = root
    decoded_string = ""
    
   
    for char in s:
        if char == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        
        if current_node.data != '\0':  
            decoded_string += current_node.data
          
            current_node = root
    
    return decoded_string


def main():
    s = input().strip()  
    freq = {}

 
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1


    root = huffman_hidden(freq)
    
  
    decoded_string = decodeHuff(root, s)
 
    print(decoded_string)

if __name__ == "__main__":
    main()
