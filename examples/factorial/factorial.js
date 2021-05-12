function factorial(n)
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

var n = 7;
var f = factorial(n);
console.log(f);
