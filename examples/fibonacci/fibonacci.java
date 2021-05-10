public class Main {
    public static void main(String[] args) {
        int a = -1;
        int b = 1;
        int i = 0;
        
        while (i < 10)
        {
            int c = a + b;
            a = b;
            b = c;
            System.out.println(c);
            i += 1;
        }
    }
}
