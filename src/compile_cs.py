import re

skip_types = ['declaration']

def upper(s): return f'{s[0].upper()}{s[1:]}'

def style_function(match_obj):
    name = match_obj.group(1)
    content = match_obj.group(2)
    return f'{upper(name)}({content})'

def get_function(function):
    if function == 'print': return 'Console.WriteLine'
    else: return upper(function)

def get_statement(statement):
    if statement == 'elif': return 'else if'
    else: return statement

def compile_cs(outpath, commands):

    program = ''
    spaces = 0

    # get import statements
    for command in commands:
        if command.type == 'function-call' and command.args[0] == 'print':
            program += 'using System;\n\n'
            break

    # open class
    program += 'class Program\n'
    program += '{\n'
    spaces += 1

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # capitalize function names
        args = [
            re.sub(
                '([a-zA-Z][a-zA-Z0-9]*)\s*\((.*)\)',
                style_function,
                arg
            )
            for arg in args
        ]

        # append spacing
        if type == 'bracket-end': program += '    ' * (spaces - 1)
        elif type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            program += f'static {args[0]} {upper(args[1])}({", ".join(args[2:])})'
        elif type == 'function-call':
            function = get_function(args[0])
            program += f'{function}({", ".join(args[1:])});'
        elif type == 'var-create': program += f'{args[0]} {args[1]};'
        elif type == 'var-set': program += f'{args[0]} {args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'array-create': program += f'{args[0]}[] {args[1]};'
        elif type == 'array-set':
            program += f'{args[0]}[] {args[1]} = {{ {", ".join(args[2:])} }};'
        elif type == 'array-update':
            program += f'{args[0]} = new {args[1]}[] {{ {", ".join(args[2:])} }};'
        elif type == 'array-index-update': program += f'{args[0]}[{args[1]}] = {args[2]};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'declaration':
            if args[0] == 'MAIN':
                program += '    static void Main()\n'
                program += '    {\n'
                spaces += 1
        elif type == 'statement-args':
            statement = get_statement(args[0])
            program += f'{statement} ({args[1]})'
        elif type == 'statement-for':
            program += f'for (int {args[0]} = {args[1]}; {args[0]} < {args[2]}; {args[0]}++)'
        elif type == 'statement-foreach':
            program += f'foreach ({args[0]} {args[1]} in {args[2]})'
        elif type == 'statement-raw': program += args[0]
        elif type == 'statement-return': program += f'return{args[0]};'
        elif type == 'bracket-start':
            program += '{'
            spaces += 1
        elif type == 'bracket-end':
            program += '}'
            spaces -= 1

        if type not in skip_types: program += '\n' # newline

    # close class
    if spaces > 1: program += '    }\n'
    program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
