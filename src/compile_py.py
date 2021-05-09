def compile_py(outpath, commands):

    program = ''

    # for each command
    for command in commands:

        type = command.type
        args = command.args

        if type == 'function-call':
            program += f'{args[0]}({", ".join(args[1:])})'
        elif type == 'var-set':
            vartype = args[0]
            value = args[2]
            if vartype == 'bool':
                if value == 'false': program += f'{args[1]} = False'
                elif value == 'true': program += f'{args[1]} = True'
                else: program += f'{args[1]} = {value}'
            else:
                program += f'{args[1]} = {value}'
        elif type == 'var-update':
            program += f'{args[0]} = {args[1]}'
        elif type == 'comment':
            program += f'# {args[0]}'

        program += '\n' # newline

    # write program to file
    file = open(outpath, 'w')
    file.write(program)
    file.close()

    print(f'compiled successfully into {outpath}')
