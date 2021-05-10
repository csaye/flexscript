public class Main {
    public static void main(String[] args) {
        int i = 1;
        
        while (i <= 100)
        {
            String output = "";
            
            if (i % 3 == 0)
            {
                output += "Fizz";
            }
            if (i % 5 == 0)
            {
                output += "Buzz";
            }
            
            if (output == "")
            {
                System.out.println(i);
            }
            else
            {
                System.out.println(output);
            }
            
            i += 1;
        }
    }
}
