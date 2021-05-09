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

## Comments

Comments are written with hashtags and translated to all languages.

```py
# this is a comment
```

## Functions

Function calls are written in `function();` syntax with any arguments separated by commas.

The `print` function is built-in and supported for all languages:

```cs
print("Hello World");
```

## Variables

Variables can be defined as `type varname = value;` and updated as `varname = newvalue;`

`int`, `double`, `char`, `string`, and `bool` types are supported for all languages.

```cs
int a = 1;
double b = 0.5;
char c = 'a';
string d = "Hello World";
bool e = false;
```

## Examples

Examples can be found in the [examples folder](examples).
