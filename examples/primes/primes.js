for (var i = 2; i < 100; i++)
{
    var prime = true;
    
    for (var j = 2; j < i; j++)
    {
        if (i % j == 0)
        {
            prime = false;
            break;
        }
    }
    
    if (prime)
    {
        console.log(i);
    }
}
