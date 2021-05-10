#_MAIN
for (int i = 1; i < 101; i++)
{
    string output = "";

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
        print(i);
    }
    else
    {
        print(output);
    }
}
