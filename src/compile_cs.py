def upper(s): return f'{s[0].upper()}{s[1:]}'

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
    program += '    static void Main()\n'
    program += '    {\n'
    spaces = 2

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # append spacing
        program += '    ' * spaces

        if type == 'function-call':
            function = args[0]
            if function == 'print':
                program += f'Console.WriteLine({args[1]});'
            else:
                program += f'{upper(args[0])}({", ".join(args[1:])});'
        elif type == 'var-set':
            program += f'{args[0]} {args[1]} = {args[2]};'
        elif type == 'var-update':
            program += f'{args[0]} = {args[1]};'
        elif type == 'comment':
            program += f'// {args[0]}'

        program += '\n'

    # close class
    program += '    }\n'
    program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
