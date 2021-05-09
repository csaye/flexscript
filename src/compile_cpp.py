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
        program += '    ' * spaces

        if type == 'function-call':
            function = args[0]
            if function == 'print':
                program += f'std::cout << {args[1]} << std::endl;'
            else:
                program += f'{args[0]}({", ".join(args[1:])});'
        elif type == 'var-set':
            vartype = args[0]
            if vartype == 'string':
                program += f'std::string {args[1]} = {args[2]};'
            else:
                program += f'{vartype} {args[1]} = {args[2]};'
        elif type == 'var-update':
            program += f'{args[0]} = {args[1]};'
        elif type == 'comment':
            program += f'// {args[0]}'

        program += '\n'

    # close class
    program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
