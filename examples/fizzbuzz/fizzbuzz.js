for (var i = 1; i < 101; i++)
{
    var output = "";
    
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
}
