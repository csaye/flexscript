let a = -1;
let b = 1;

for (let i = 0; i < 10; i++)
{
    let c = a + b;
    a = b;
    b = c;
    console.log(c);
}
