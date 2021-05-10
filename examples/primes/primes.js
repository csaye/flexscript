i = 2;
j = 2;

while (i < 100)
{
    prime = true;
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
        console.log(i);
    }
    
    i += 1;
}
