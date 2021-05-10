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
    program += 'public class Main {\n'
    program += '    public static void main(String[] args) {\n'
    spaces = 2

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # append spacing
        if type != 'bracket-end': program += '    ' * spaces
        else: program += '    ' * (spaces - 1)

        if type == 'function-call':
            function = get_function(args[0])
            program += f'{function}({", ".join(args[1:])});'
        elif type == 'var-create':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]};'
        elif type == 'var-set':
            vartype = get_vartype(args[0])
            program += f'{vartype} {args[1]} = {args[2]};'
        elif type == 'var-update': program += f'{" ".join(args)};'
        elif type == 'comment': program += f'// {args[0]}'
        elif type == 'statement-args':
            statement = get_statement(args[0])
            program += f'{statement} ({args[1]})'
        elif type == 'statement-else': program += 'else'
        elif type == 'bracket-start':
            program += '{'
            spaces += 1
        elif type == 'bracket-end':
            program += '}'
            spaces -= 1

        program += '\n'

    # close class
    program += '    }\n'
    program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
