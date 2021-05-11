int factorial(int n)
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

#_MAIN
int n = 7;
int f = factorial(n);
print(f);
