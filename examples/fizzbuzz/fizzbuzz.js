i = 1;

while (i <= 100)
{
    output = "";
    
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
        console.log(i);
    }
    else
    {
        console.log(output);
    }
    
    i += 1;
}
