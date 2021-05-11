public class Main
{
    static int factorial(int n)
    {
        if (n < 2)
        {
            return n;
        }
        else
        {
            return n * factorial(n - 1);
        }
    }
    
    public static void main(String[] args)
    {
        int n = 7;
        int f = factorial(n);
        System.out.println(f);
    }
}
