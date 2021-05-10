public class Main {
    public static void main(String[] args) {
        int i = 2;
        int j = 2;
        
        while (i < 100)
        {
            boolean prime = true;
            j = 2;
            
            while (j < i)
            {
                if (i % j == 0)
                {
                    prime = false;
                }
                
                j += 1;
            }
            
            if (prime)
            {
                System.out.println(i);
            }
            
            i += 1;
        }
    }
}
