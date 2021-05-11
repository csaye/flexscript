factorial(n)
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

let n = 7;
let f = factorial(n);
console.log(f);
