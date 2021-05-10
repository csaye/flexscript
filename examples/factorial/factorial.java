public class Main
{
    public static void main(String[] args)
    {
        int n = 7;
        int f = 1;
        
        while (n > 1)
        {
            f *= n;
            n -= 1;
        }
        
        System.out.println(f);
    }
}
