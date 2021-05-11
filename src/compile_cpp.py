skip_types = ['declaration']

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
            program += f'{vartype} {args[1]}({", ".join(args[2:])})'
        elif type == 'function-call':
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
        elif type == 'declaration':
            if args[0] == 'MAIN':
                program += 'int main()\n'
                program += '{\n'
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
    if spaces > 0: program += '}\n'

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
