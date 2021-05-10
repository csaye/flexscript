def get_vartype(vartype):
    if vartype == 'string': return 'std::string'
    else: return vartype

def get_statement(statement):
    if statement == 'elif': return 'else if'
    else: return statement

def compile_cpp(outpath, commands):

    program = ''
    spaces = 0

    # get import statements
    for command in commands:
        if command.type == 'function-call' and command.args[0] == 'print':
            program += '#include <iostream>\n\n'
            break

    # open class
    program += 'int main()\n'
    program += '{\n'
    spaces = 1

    # for each command
    for command in commands:

        # get command data
        type = command.type
        args = command.args

        # append spacing
        if type != 'bracket-end': program += '    ' * spaces
        else: program += '    ' * (spaces - 1)

        if type == 'function-call':
            function = args[0]
            if function == 'print':
                program += f'std::cout << {args[1]} << std::endl;'
            else:
                program += f'{args[0]}({", ".join(args[1:])});'
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
    program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
