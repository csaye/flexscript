int a = -1;
int b = 1;
int i = 0;

while (i < 10)
{
    int c = a + b;
    a = b;
    b = c;
    print(c);
    i += 1;
}
