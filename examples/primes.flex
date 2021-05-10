#_MAIN
for (int i = 2; i < 100; i++)
{
    bool prime = true;

    for (int j = 2; j < i; i++)
    {
        if (i % j == 0)
        {
            prime = false;
        }
    }

    if (prime)
    {
        print(i);
    }
}
