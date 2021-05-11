skip_types = ['declaration']

def get_vartype(vartype):
    if vartype == 'string': return 'String'
    elif vartype == 'bool': return 'boolean'
    else: return vartype

def get_function(function):
    if function == 'print': return 'System.out.println'
    else: return function

def get_statement(statement):
    if statement == 'elif': return 'else if'
    else: return statement

def compile_java(outpath, commands):

    program = ''
    spaces = 0

    # open class
    program += 'public class Main\n'
    program += '{\n'
    spaces += 1

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # append spacing
        if type == 'bracket-end': program += '    ' * (spaces - 1)
        elif type not in skip_types: program += '    ' * spaces

        if type == 'function-def':
            vartype = get_vartype(args[0])
            program += f'static {vartype} {args[1]}({", ".join(args[2:])})'
        elif type == 'function-call':
            function = get_function(args[0])
            program += f'{function}({", ".join(args[1:])});'
        elif type == 'var-create':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]};'
        elif type == 'var-set':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'array-set':
            vartype = get_vartype(args[0])
            program += f'{vartype}[] {args[1]} = {{ {", ".join(args[2:])} }};'
        elif type == 'array-update': program += f'{args[0]}[{args[1]}] = {args[2]};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'declaration':
            if args[0] == 'MAIN':
                program += '    public static void main(String[] args)\n'
                program += '    {\n'
                spaces += 1
        elif type == 'statement-args':
            statement = get_statement(args[0])
            program += f'{statement} ({args[1]})'
        elif type == 'statement-for':
            program += f'for (int {args[0]} = {args[1]}; {args[0]} < {args[2]}; {args[0]}++)'
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
