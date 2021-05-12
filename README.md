# FlexScript

<img width="448px" src="https://user-images.githubusercontent.com/27871609/117590506-0c98a480-b0ed-11eb-9699-ecc3353e6a8b.png">

A programming language that compiles into multiple languages.

Currently supports Python, JavaScript, C#, Java, and C++.

## Installation/Compilation

In order to install FlexScript, clone the project:

```bash
git clone https://github.com/csaye/flexscript
cd flexscript/
```

Then compile your .flex file like so:

```
./compile.sh <program.flex> <py | js | cs | java | cpp | all>
```

If necessary, give permission to execute `compile.sh`:

```
chmod +x compile.sh
```

## Comments

Comments are written with hashtags and translated to all languages:

```py
# this is a comment
```

If a comment begins with an underscore, it is parsed as a declaration:

```cs
#_MAIN
```

`#_MAIN` is used once to define where global class declarations end.

## Variables

Variables can be defined with `type varname;` or `type varname = value;` and updated with `varname = value;`

`int`, `double`, `char`, `string`, and `bool` types are supported for all languages:

```cs
int a = 1;
double b = 0.5;
char c = 'a';
string d = "Hello World";
bool e = false;
```

## Arrays

Arrays can be defined with `type[] varname;` or `type[] varname = {};`

Arrays can be updated with `varname = type {};` and `varname[index] = value;`

```cs
int[] unset;
unset = int { 1, 2, 3 };
int[] array = { 1, 2, 3 };
array[1] = 0;
print(array[1]);
```

## Functions

Function calls are written in `function();` syntax with any arguments separated by commas.

The `print` function is built-in and supported for all languages:

```cs
print("Hello World");
```

Function definitions are written in `type function() {}` syntax and should be done before `#_MAIN`:

```cs
void helloworld()
{
    print("Hello World");
}

#_MAIN
helloworld();
```

## Conditional Statements

Conditional statements are written in the form `statement (condition) {}`.

`if/elif/else (condition)` statements:

```py
if (false)
{
    print("false");
}
elif (false)
{
    print("false");
}
else
{
    print("true");
}
```

`while (condition)` statements:

```cs
int i = 0;

while (i < 10)
{
    print(i);
    i += 1;
}
```

`for (int varname = low; varname < high; varname++)` statements:

```cs
for (int i = 0; i < 10; i++)
{
    print(i);
}
```

`foreach (type varname in varname) statements`:

```cs
int[] array = { 1, 2, 3 };

foreach (int num in array)
{
    print(num);
}
```

## Examples

[HelloWorld.flex](examples/helloworld.flex)

Prints "Hello World".

```cs
#_MAIN
print("Hello World");
```

[Fibonacci.flex](examples/fibonacci.flex)

Prints the first 10 numbers of the Fibonacci sequence.

```cs
#_MAIN
int a = -1;
int b = 1;

for (int i = 0; i < 10; i++)
{
    int c = a + b;
    a = b;
    b = c;
    print(c);
}
```

[FizzBuzz.flex](examples/fizzbuzz.flex)

Prints numbers 1 to 100 (inclusive), replacing every multiple of 3 with "Fizz", every multiple of 5 with "Buzz", and every multiple of both with "FizzBuzz".

```cs
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
```

[Primes.flex](examples/primes.flex)

Prints all prime numbers up to 100.

```cs
#_MAIN
for (int i = 2; i < 100; i++)
{
    bool prime = true;

    for (int j = 2; j < i; i++)
    {
        if (i % j == 0)
        {
            prime = false;
            break;
        }
    }

    if (prime)
    {
        print(i);
    }
}
```

[Factorial.flex](examples/factorial.flex)

Computes and prints the factorial of n using recursion.

```cs
int factorial(int n)
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

#_MAIN
int n = 7;
int f = factorial(n);
print(f);
```

More examples can be found in the [examples folder](examples).
