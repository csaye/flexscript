a = -1;
b = 1;
i = 0;

while (i < 10)
{
    c = a + b;
    a = b;
    b = c;
    console.log(c);
    i += 1;
}
