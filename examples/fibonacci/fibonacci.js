var a = -1;
var b = 1;

for (var i = 0; i < 10; i++)
{
    var c = a + b;
    a = b;
    b = c;
    console.log(c);
}
